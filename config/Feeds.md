---
timezone: America/Chicago
rss:
  - name: "Nates Notebook"
    url: "https://api.substack.com/feed/podcast/1373231.rss"
ical:
  - name: "Google Calendar"
    url: "https://example.com/calendar.ics"
---

# Feed Config

Feed URLs for the `/feeds` skill. Edit the frontmatter to add or remove feeds.

Set `timezone:` to your IANA zone (e.g. `America/Chicago`, `America/New_York`, `Europe/London`). Events with UTC times in the source feed get converted to this zone before being written to the cached iCal notes. If omitted, falls back to UTC.

## RSS Feeds

Each RSS feed gets a folder at `01 Raw Sources/RSS - {name}/`. One note per item, deduped by GUID.

## iCal Feeds

Each iCal feed gets a maintained note at `02 Calendar/iCal Feeds/{name}.md`. Run `/feeds ical` to refresh. The daily agent reads from these notes.
