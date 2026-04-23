---
name: focus
description: Pick a MOC and load all linked notes into context for a deep work session, with a session log pinned to today's daily note.
argument-hint: MOC name or path (defaults to active note)
allowed-tools: Bash, Read, Write, Edit, Grep
---

Start a focus session on a Map of Content. $ARGUMENTS: MOC name or path. If no argument, use the currently active Obsidian note.

---

## Step 1: Resolve the MOC

If no argument provided, get the active note:
```bash
obsidian file
```
Grab the `path` row from the output.

If an argument is provided, use CLI name resolution:
```bash
obsidian read file="$ARGUMENTS"
```

Read the resolved note. Check its frontmatter for a `#moc` tag. If the tag is missing, ask: "This note isn't a MOC yet — want me to run `/moc` on it first, or continue anyway?"

If the user wants `/moc` first, stop and let them invoke it. If they say continue, proceed.

---

## Step 2: Extract and load linked notes

Extract all `[[wikilinks]]` from the MOC body (ignore links inside Dataview codeblocks).

For each wikilink, use CLI name resolution to read the note:
```bash
obsidian read file="<wikilink name>"
```

- If the file is **< 200 lines** — read the whole thing
- If the file is **>= 200 lines** — read the first 80 lines only
- If the CLI returns an error — note it as a stub/missing

Do this in parallel batches for speed.

Record for each note:
- Path (from CLI output or `obsidian file info`)
- Line count
- Whether it was fully loaded or truncated
- Whether it's a stub (missing file)

---

## Step 3: Recency analysis

Run in parallel:
- `git log --name-only --pretty=format:"%h %ai %s" -20 -- "<path>"` for each linked note's parent folder (deduplicated)
- `obsidian recents`

From the results, determine:
- Which linked notes were modified most recently and when
- Which appear in Obsidian recents (actively being viewed)
- Which haven't been touched in a while

Filter `.tmp` files from recents output — these are editor artifacts, not real notes.

---

## Step 4: Where you left off

Synthesize a brief "state of the project" covering:
- **Active edges** — notes recently modified or with in-progress content (TODOs, empty sections, placeholder text)
- **Stubs** — wikilinks that don't have a note yet
- **Mature notes** — notes that look complete or haven't been touched recently
- **Coverage gaps** — if the MOC has a "Coverage Gaps" section, surface those items

Keep this to a concise paragraph or short bullet list. This is a read of the landscape, not a dump of content.

---

## Step 5: Start the session log

Get today's date from the `currentDate` context value. Read the daily note:
```bash
obsidian daily:read
```

If the daily note does not exist, create it:
```bash
obsidian daily
```
Then read it.

Check if a `## Focus Sessions` heading already exists at the bottom of the daily note.

- If **no** — append a new `## Focus Sessions` section at the very end of the file
- If **yes** — append a new `###` entry under the existing section

Append this entry using Edit:

```markdown
### {MOC Title} — {HH:MM}
**MOC:** [[{MOC Title}]]
**Loaded:** {N} notes ({M} truncated, {S} stubs)
**State:** {one-sentence summary of where things stand}
**Activity:**
```

The `**Activity:**` section starts empty. During the session, append a line each time:
- The user confirms a decision
- A note is created, edited, or moved
- A structural change is made (new section, new link added to MOC)

Format each activity line as:
```
- {HH:MM} — {what was confirmed or executed}
```

Do NOT log:
- Drafts or generations that get corrected
- Read-only exploration
- Back-and-forth discussion before a decision

---

## Step 6: Present the session

Output:
1. The "where you left off" synthesis from Step 4
2. A list of loaded notes with status indicators: `[full]`, `[truncated]`, `[stub]`
3. "Focus session started — logging to [[{DATE}]]."
4. "Where do you want to dig in?"
