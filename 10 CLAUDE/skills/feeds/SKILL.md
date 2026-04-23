---
name: feeds
description: RSS and iCal feed integrator — fetch RSS items into Raw Sources, maintain iCal feed notes in Calendar.
argument-hint: "[rss|ical|all|list|add rss <name> <url>|add ical <name> <url>]"
allowed-tools: Bash, Read, Edit
---

Manage RSS and iCal feeds for this vault. Config lives in `config/feeds.md` (YAML frontmatter). Scripts live in `10 CLAUDE/skills/feeds/scripts/`.

Route by $ARGUMENTS:

| Pattern | Action |
|---------|--------|
| *(empty)* or `all` | Sync all RSS + iCal feeds |
| `rss` | Sync RSS feeds only |
| `ical` | Sync iCal feeds only |
| `list` | Show all configured feeds |
| `add rss <name> <url>` | Add an RSS feed to config |
| `add ical <name> <url>` | Add an iCal feed to config |

---

## Sync RSS (`rss` or `all`)

```bash
"$HOME/.venvs/claude/Scripts/python.exe" "10 CLAUDE/skills/feeds/scripts/fetch_rss.py"
```

Output lines beginning with `NEW:` are new notes created. Report a summary: how many new items per feed, where they landed (`01 Raw Sources/RSS - {name}/`).

---

## Sync iCal (`ical` or `all`)

```bash
"$HOME/.venvs/claude/Scripts/python.exe" "10 CLAUDE/skills/feeds/scripts/fetch_ical.py"
```

Report which feed notes were updated and event counts. Notes land in `02 Calendar/iCal Feeds/`.

---

## List feeds (`list`)

Read `config/feeds.md` and display the RSS and iCal entries from the frontmatter in a readable table.

---

## Add feed (`add rss <name> <url>` or `add ical <name> <url>`)

1. Read `config/feeds.md`
2. Parse the frontmatter
3. Append the new entry to the appropriate list (`rss` or `ical`) in the frontmatter
4. Write the file back with Edit
5. Confirm: "Added {type} feed '{name}' → `config/feeds.md`"

---

## Output locations

- **RSS items:** `01 Raw Sources/RSS - {FeedName}/` — one `.md` note per item
- **iCal notes:** `02 Calendar/iCal Feeds/{FeedName}.md` — one note per feed, full event dump

## iCal note format

Each iCal feed note has YAML frontmatter (`feed_name`, `feed_url`, `last_synced`, `event_count`, `tags`) followed by events grouped by date:

```
## 2026-04-15 (Tuesday)

### 10:00 AM – 11:00 AM | Meeting Title
- **Location:** Zoom
- **Description:** …
- **UID:** `uid@domain`
```

The daily agent can grep this note by date heading to surface events for a given day.

## Dependencies

- `feedparser` — RSS/Atom parsing
- `icalendar` — iCal parsing
- `httpx` — HTTP fetching
- `python-frontmatter` — config and note frontmatter

If a script fails with `ModuleNotFoundError`, run:
```bash
uv pip install feedparser icalendar --python "$HOME/.venvs/claude/Scripts/python.exe"
```
