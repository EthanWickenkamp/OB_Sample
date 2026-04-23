#!/usr/bin/env python3
"""
Fetch RSS feeds and create notes in 01 Raw Sources/RSS - {name}/
One note per item, deduped by GUID/link.
Usage: python fetch_rss.py [--dry-run]
"""
import sys
import re
import hashlib
import html
from pathlib import Path
from datetime import datetime, timezone

try:
    import feedparser
except ImportError:
    print("ERROR: feedparser not installed. Run: uv pip install feedparser --python \"$HOME/.venvs/claude/Scripts/python.exe\"")
    sys.exit(1)

try:
    import frontmatter
except ImportError:
    print("ERROR: python-frontmatter not installed.")
    sys.exit(1)

VAULT_ROOT = Path(__file__).parents[4]
CONFIG_FILE = VAULT_ROOT / "config" / "feeds.md"
RAW_SOURCES = VAULT_ROOT / "01 Raw Sources"


def slugify(text):
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[-\s]+", "-", text).strip("-")
    return text[:80]


def load_rss_config():
    if not CONFIG_FILE.exists():
        print(f"ERROR: Config file not found: {CONFIG_FILE}")
        sys.exit(1)
    post = frontmatter.load(str(CONFIG_FILE))
    return post.get("rss", [])


def get_existing_guids(folder: Path) -> set:
    guids = set()
    if not folder.exists():
        return guids
    for note in folder.glob("*.md"):
        try:
            post = frontmatter.load(str(note))
            guid = post.get("guid")
            if guid:
                guids.add(str(guid))
        except Exception:
            pass
    return guids


def strip_html(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = html.unescape(text)
    return text.strip()


def entry_to_note(entry, feed_name: str):
    title = html.unescape(getattr(entry, "title", "Untitled"))
    link = getattr(entry, "link", "")
    guid = str(getattr(entry, "id", link) or link)

    published = ""
    for attr in ("published_parsed", "updated_parsed"):
        val = getattr(entry, attr, None)
        if val:
            dt = datetime(*val[:6], tzinfo=timezone.utc)
            published = dt.strftime("%Y-%m-%d")
            break

    content = ""
    if hasattr(entry, "content") and entry.content:
        content = entry.content[0].get("value", "")
    elif hasattr(entry, "summary"):
        content = entry.summary or ""
    content = strip_html(content)

    # Podcast-specific fields
    duration = getattr(entry, "itunes_duration", None)

    body_parts = []
    if content:
        body_parts.append(content)
    if link:
        body_parts.append(f"\n[Read original]({link})")

    fm = {
        "feed": feed_name,
        "guid": guid,
        "source": link,
        "published": published,
        "ingested": datetime.now().strftime("%Y-%m-%d"),
        "tags": ["rss", slugify(feed_name)],
    }
    if duration:
        fm["duration"] = duration

    return frontmatter.Post("\n".join(body_parts), **fm), title, guid


def main():
    dry_run = "--dry-run" in sys.argv
    feeds = load_rss_config()

    if not feeds:
        print("No RSS feeds configured.")
        return

    total_new = 0
    for feed_cfg in feeds:
        name = feed_cfg.get("name", "Unknown")
        url = feed_cfg.get("url", "")
        if not url or "example.com" in url:
            print(f"SKIP: {name} (placeholder URL)")
            continue

        print(f"Fetching: {name}")
        parsed = feedparser.parse(url)

        if parsed.bozo and not parsed.entries:
            print(f"  ERROR: Could not parse feed ({parsed.bozo_exception})")
            continue

        folder = RAW_SOURCES / f"RSS - {name}"
        existing_guids = get_existing_guids(folder)

        new_count = 0
        for entry in parsed.entries:
            post, title, guid = entry_to_note(entry, name)
            if guid in existing_guids:
                continue

            filename = slugify(title) + ".md"
            note_path = folder / filename
            if note_path.exists():
                h = hashlib.md5(guid.encode()).hexdigest()[:6]
                note_path = folder / f"{slugify(title)}-{h}.md"

            if not dry_run:
                folder.mkdir(parents=True, exist_ok=True)
                note_path.write_text(frontmatter.dumps(post), encoding="utf-8")

            print(f"  NEW: {title}")
            new_count += 1

        total_new += new_count
        print(f"  -> {new_count} new items from {name}")

    print(f"\nTotal: {total_new} new items ingested.")


if __name__ == "__main__":
    main()
