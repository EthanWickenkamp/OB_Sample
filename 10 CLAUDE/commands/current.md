---
name: current
description: Load the currently active Obsidian note into context.
allowed-tools: Bash
---

Run `obsidian file`, grab the `path` row, Read that path. If `obsidian file` fails, report Obsidian not running and stop.

Reply:
- `Loaded: <path>`
- One sentence on the note
- "Where do you want to pick up?"
