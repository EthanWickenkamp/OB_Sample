---
name: daily
description: Daily note hub — view, add to-dos, add events, show upcoming. Single entry point for all daily note operations.
argument-hint: "[todo|event|upcoming] [YYYY-MM-DD] [args]"
allowed-tools: Bash, Read, Edit
---

Daily note management. Route by $ARGUMENTS:

| Pattern | Action |
|---------|--------|
| *(empty)* | Load today's daily note |
| `todo [DATE] description` | Add a to-do |
| `event [DATE] [TIME] description` | Add an event |
| `upcoming` | Show upcoming events |

DATE defaults to today if omitted. Get today from the `currentDate` context value.

---

## Load daily note (no args)

```bash
obsidian daily:read
```

If it doesn't exist, run `obsidian daily` to create it. Show the full content and resolved path.

---

## todo [DATE] description

Add a to-do item under `### To Do`.

1. Read the note:
```bash
obsidian read path="02 Calendar/{DATE}.md"
```
If it doesn't exist, create it:
```bash
obsidian create path="02 Calendar/{DATE}.md" template="Daily"
```

2. Use the Edit tool to insert `- [ ] {Description}` under `### To Do` (after any existing items, before the next heading).

3. Confirm: "Added to-do '{Description}' to {DATE}"

---

## event [DATE] [TIME] description

Add an event under `### Events`.

1. Parse: DATE is first token. Next token(s) are time if they match 12-hour pattern (e.g. "1:30 PM"). Convert 24-hour input to 12-hour AM/PM. Rest is description. If no time given, omit it.

2. Read/create the note (same as todo above).

3. Use the Edit tool to insert under `### Events`:
   - With time: `- {H:MM AM/PM} {Description}`
   - Without time: `- {Description}`

4. Confirm with one-line summary.

---

## upcoming

Show all upcoming events across daily notes.

1. List daily notes:
```bash
obsidian files folder="02 Calendar" ext=md
```
Filter to filenames matching `YYYY-MM-DD.md`, keep dates >= today.

2. Read each qualifying note, extract lines under `### Events` (between `### Events` and next `###`). Keep lines starting with `- `.

3. Display grouped by date. If none, say "No upcoming events."

---

## Obsidian CLI daily reference

```
obsidian daily                          Open today's daily note (creates if needed)
obsidian daily:read                     Read daily note contents into context
obsidian daily:path                     Get daily note file path
obsidian daily:append content=<text>    Append to daily note
obsidian daily:prepend content=<text>   Prepend to daily note
obsidian tasks daily                    List tasks from daily note
obsidian tasks daily todo               Incomplete tasks from daily note
obsidian tasks daily done               Completed tasks from daily note
obsidian read path="02 Calendar/{DATE}.md"   Read a specific date's note
obsidian create path="02 Calendar/{DATE}.md" template="Daily"   Create a specific date's note
```
