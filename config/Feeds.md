---
rss:
  - name: "Nates Notebook"
    url: "https://api.substack.com/feed/podcast/1373231.rss"
ical:
  - name: "Google Calendar"
    url: "https://example.com/calendar.ics"
---

# Feed Config

Feed URLs for the `/feeds` skill. Edit the frontmatter to add or remove feeds.

## RSS Feeds

Each RSS feed gets a folder at `01 Raw Sources/RSS - {name}/`. One note per item, deduped by GUID.

## iCal Feeds

Each iCal feed gets a maintained note at `02 Calendar/iCal Feeds/{name}.md`. Run `/feeds ical` to refresh. The daily agent reads from these notes.
