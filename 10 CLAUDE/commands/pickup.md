---
name: pickup
description: Summarize recent vault activity to catch up on where you left off.
allowed-tools: Read, Bash
---

Help the user pick up where they left off by summarizing recent vault activity. No arguments.

## Steps

1. Run `obsidian recents` via Bash to get recently opened files. Filter out `.tmp` files (editor artifacts).
2. Read HOME.md at the vault root to see the "Current" section (pinned projects).
3. Read daily notes for yesterday, today, and tomorrow (`02 Calendar/YYYY-MM-DD.md`). Skip any that don't exist.
4. Read the 3–5 most recently modified notes from the recents list (skip attachments, daily notes in `02 Calendar/`, and config files).
5. Synthesize a brief, conversational summary covering:
   - What's on the calendar / to-do list across the three days
   - What projects/topics appear to be active (from HOME.md Current and Pinned sections)
   - What the recent notes are about and any notable content (open questions, todos, decisions, work in progress)
   - A 1-2 sentence "where you left off" takeaway

Keep the summary concise — bullet points are fine. Don't dump raw note content; distill it.
