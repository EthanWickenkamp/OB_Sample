
# Vault Task Management

## What

A two-stage system that keeps TODO items across the vault accurate, personalized, and current. Runs as a scheduled morning job on SilverFish before the day starts.

**Stage 1 — Python iCal fetcher** (cron, stateless)
Pulls D2L calendar feeds for all active courses, parses events/assignments, writes structured output for Claude to consume.

**Stage 2 — Claude agent** (triggered after Stage 1)
Reads the iCal output alongside course notes, week notes, project notes, and recent vault activity. Produces:
- Personalized TODO items in each course note (Tasks plugin emoji format)
- Note stubs for new assignments/events that warrant their own page
- A morning summary in today's daily note

## Obsidian Tasks Plugin

Installed and active. Uses emoji format for metadata:

| Emoji | Meaning | Example |
|-------|---------|---------|
| `📅` | Due date | `📅 2026-04-19` |
| `⏳` | Scheduled date | `⏳ 2026-04-15` |
| `🔺` | High priority | |
| `🔼` | Medium priority | |
| `🔽` | Low priority | |
| `✅` | Done date (auto) | `✅ 2026-04-02` |

Tasks are standard `- [ ]` checkboxes with emoji metadata appended. The plugin auto-suggests metadata when typing in a task line.

### Query Location

[[Spring 2026]] has a live Tasks query dashboard that pulls incomplete tasks from the four main course notes only (not sub-pages like Project 1). Queries are grouped by: Overdue, Due This Week, Coming Up (30 days), No Due Date.

## Data Sources

### iCal Feeds (D2L)

Private token feeds — no auth needed beyond the URL. One per course:
`https://d2l.depaul.edu/d2l/le/calendar/feed/user/feed.ics?feedOU=#&token=#`

### Vault Activity

Claude reads recent git history, week notes, and project notes to understand what the user has been working on. This context makes TODO items actionable rather than generic.

### Future Sources

Other data sources can be added as the system matures (GitHub issues, homelab alerts, etc.)

## Morning Briefing

Written into today's daily note as a `## Morning Briefing` section. Contains:

- **What's due** — upcoming deadlines with context from course notes
- **Where you left off** — based on recent vault edits and git history
- **Course schedule** — what topics are covered in today's classes
- **Study tidbits** — relevant concept refreshers tied to upcoming material (e.g., "CSE 333 moves to Fourier Series this week — builds on LTI convolution from last week")

## Architecture

```
SilverFish (cron, ~6am daily)
  │
  ├─ Stage 1: Python script
  │    ├─ Fetch 4 iCal feeds
  │    ├─ Parse VEVENT items
  │    └─ Write markdown to 12 Calendar/iCalFeeds/
  │
  └─ Stage 2: Claude agent
       ├─ Read iCal output
       ├─ Read course notes, week notes, project notes
       ├─ Read recent git log for vault activity
       ├─ Update/create TODO items in course notes (Tasks emoji format)
       ├─ Create note stubs for new assignments
       ├─ Write Morning Briefing to today's daily note
       └─ Git commit + push to Gitea
```

All clients (Windows PC, laptop, phone) pull the result via normal git sync.

## Implementation Status

- [x] Obsidian Tasks plugin installed and configured
- [x] Tasks emoji format in use across course notes
- [x] Live Tasks query dashboard in [[Spring 2026]]
- [x] iCal feed links in all four course notes
- [ ] Python iCal fetcher script
- [ ] Claude morning agent prompt
- [ ] SilverFish cron job setup
- [ ] Morning Briefing template/format in daily notes
