#!/usr/bin/env python3
"""
Fetch iCal feeds and maintain notes in 02 Calendar/iCal Feeds/
One note per feed, refreshed on every run.
Usage: python fetch_ical.py [--dry-run]
"""
import sys
from pathlib import Path
from datetime import datetime, date, timedelta, timezone

try:
    import httpx
except ImportError:
    print("ERROR: httpx not installed.")
    sys.exit(1)

try:
    from icalendar import Calendar
    import icalendar
except ImportError:
    print("ERROR: icalendar not installed. Run: uv pip install icalendar --python \"$HOME/.venvs/claude/Scripts/python.exe\"")
    sys.exit(1)

try:
    import frontmatter
except ImportError:
    print("ERROR: python-frontmatter not installed.")
    sys.exit(1)

VAULT_ROOT = Path(__file__).parents[4]
CONFIG_FILE = VAULT_ROOT / "config" / "feeds.md"
ICAL_FOLDER = VAULT_ROOT / "02 Calendar" / "iCal Feeds"
LOOKAHEAD_DAYS = 90


def load_ical_config():
    if not CONFIG_FILE.exists():
        print(f"ERROR: Config file not found: {CONFIG_FILE}")
        sys.exit(1)
    post = frontmatter.load(str(CONFIG_FILE))
    return post.get("ical", [])


def to_date(dt_val):
    if isinstance(dt_val, datetime):
        return dt_val.date()
    if isinstance(dt_val, date):
        return dt_val
    return None


def fmt_time(dt_val):
    """Return '1:30 PM' string or None for all-day events."""
    if isinstance(dt_val, datetime):
        return dt_val.strftime("%I:%M %p").lstrip("0")
    return None


def expand_recurring(component, today, cutoff):
    """
    Return a list of occurrence dates for a VEVENT component.
    Handles simple RRULE (DAILY/WEEKLY/MONTHLY) without exotic modifiers.
    Falls back to single occurrence if RRULE is complex or absent.
    """
    dtstart = component.get("DTSTART")
    if not dtstart:
        return []

    start_val = dtstart.dt
    start_date = to_date(start_val)
    if not start_date:
        return []

    rrule = component.get("RRULE")
    if not rrule:
        return [start_date] if today <= start_date <= cutoff else []

    # Basic RRULE expansion
    freq = str(rrule.get("FREQ", ["DAILY"])[0]).upper()
    interval = int(rrule.get("INTERVAL", [1])[0])
    until_list = rrule.get("UNTIL", [])
    count_list = rrule.get("COUNT", [])

    until = None
    if until_list:
        u = until_list[0]
        until = u.date() if isinstance(u, datetime) else u
    if until and until < today:
        return []

    step = {"DAILY": timedelta(days=interval),
            "WEEKLY": timedelta(weeks=interval),
            "MONTHLY": None}.get(freq)

    if step is None and freq != "MONTHLY":
        # Unsupported freq — just return original if in range
        return [start_date] if today <= start_date <= cutoff else []

    occurrences = []
    current = start_date
    count = 0
    max_count = int(count_list[0]) if count_list else 10000

    while current <= cutoff and count < max_count:
        if current >= today:
            occurrences.append(current)
        if freq == "MONTHLY":
            # Advance by one month, same day
            month = current.month + interval
            year = current.year + (month - 1) // 12
            month = (month - 1) % 12 + 1
            try:
                current = current.replace(year=year, month=month)
            except ValueError:
                break
        else:
            current += step
        count += 1
        if until and current > until:
            break

    return occurrences


def build_feed_note(feed_name, feed_url, events_by_date):
    now = datetime.now()
    lines = [
        f"*Last synced: {now.strftime('%Y-%m-%d %I:%M %p')}*",
        "",
    ]

    if not events_by_date:
        lines.append("*No upcoming events in the next 90 days.*")
    else:
        for d in sorted(events_by_date.keys()):
            lines += ["---", "", f"## {d.strftime('%Y-%m-%d (%A)')}", ""]
            for evt in sorted(events_by_date[d], key=lambda e: e["sort_key"]):
                if evt["all_day"]:
                    lines.append(f"### All Day | {evt['summary']}")
                else:
                    end_str = f" – {evt['end_time']}" if evt.get("end_time") else ""
                    lines.append(f"### {evt['start_time']}{end_str} | {evt['summary']}")
                if evt.get("location"):
                    lines.append(f"- **Location:** {evt['location']}")
                if evt.get("description"):
                    desc = evt["description"].strip().replace("\n", " ")
                    if len(desc) > 300:
                        desc = desc[:300] + "…"
                    lines.append(f"- **Description:** {desc}")
                lines.append(f"- **UID:** `{evt['uid']}`")
                lines.append("")

    body = "\n".join(lines)
    fm = {
        "feed_name": feed_name,
        "feed_url": feed_url,
        "last_synced": now.strftime("%Y-%m-%dT%H:%M:%S"),
        "event_count": sum(len(v) for v in events_by_date.values()),
        "tags": ["ical", "calendar"],
    }
    return frontmatter.Post(body, **fm)


def main():
    dry_run = "--dry-run" in sys.argv
    feeds = load_ical_config()

    if not feeds:
        print("No iCal feeds configured.")
        return

    today = date.today()
    cutoff = today + timedelta(days=LOOKAHEAD_DAYS)

    if not dry_run:
        ICAL_FOLDER.mkdir(parents=True, exist_ok=True)

    for feed_cfg in feeds:
        name = feed_cfg.get("name", "Unknown")
        url = feed_cfg.get("url", "")
        if not url or "example.com" in url:
            print(f"SKIP: {name} (placeholder URL)")
            continue

        print(f"Fetching: {name}")

        try:
            response = httpx.get(url, timeout=30, follow_redirects=True)
            response.raise_for_status()
        except Exception as e:
            print(f"  ERROR: Could not fetch feed: {e}")
            continue

        try:
            cal = Calendar.from_ical(response.content)
        except Exception as e:
            print(f"  ERROR: Could not parse iCal data: {e}")
            continue

        events_by_date: dict[date, list] = {}

        for component in cal.walk():
            if component.name != "VEVENT":
                continue

            dtstart = component.get("DTSTART")
            if not dtstart:
                continue

            start_val = dtstart.dt
            all_day = not isinstance(start_val, datetime)
            start_time = fmt_time(start_val)

            dtend = component.get("DTEND")
            end_val = dtend.dt if dtend else None
            end_time = fmt_time(end_val) if end_val else None

            summary = str(component.get("SUMMARY", "Untitled"))
            location = str(component.get("LOCATION", "")).strip() or None
            description = str(component.get("DESCRIPTION", "")).strip() or None
            uid = str(component.get("UID", ""))

            occurrences = expand_recurring(component, today, cutoff)
            for occ_date in occurrences:
                evt = {
                    "summary": summary,
                    "all_day": all_day,
                    "start_time": start_time,
                    "end_time": end_time,
                    "location": location,
                    "description": description,
                    "uid": uid,
                    "sort_key": start_time or "00:00 AM",
                }
                events_by_date.setdefault(occ_date, []).append(evt)

        event_count = sum(len(v) for v in events_by_date.values())
        print(f"  -> {event_count} events across {len(events_by_date)} days")

        post = build_feed_note(name, url, events_by_date)
        note_path = ICAL_FOLDER / f"{name}.md"

        if not dry_run:
            note_path.write_text(frontmatter.dumps(post), encoding="utf-8")
            print(f"  -> Written: 02 Calendar/iCal Feeds/{name}.md")
        else:
            print(f"  -> DRY RUN: would write 02 Calendar/iCal Feeds/{name}.md")

    print("\nDone.")


if __name__ == "__main__":
    main()
