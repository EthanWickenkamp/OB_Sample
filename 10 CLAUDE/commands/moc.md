---
description: Generate a Map of Content (MOC) for a folder — auto-index of all notes grouped by subfolder, stored in 05 Menus/.
argument-hint: folder path or Notes subfolder name
allowed-tools: Bash, Read, Write, Edit
---

Generate a Map of Content (MOC) for a folder. $ARGUMENTS: folder path or subfolder name under `04 Notes/`.

A MOC is a structural navigation index — it maps what exists in a folder, grouped by subfolder. It is not curated or editorial; it is automatic and complete. For curated/distilled notes — where you bring your own structure and ideas to a topic — use `/crystal` instead.

---

## Step 1: Resolve folder

Run in parallel:
```bash
obsidian files folder="{ARG}"
obsidian files folder="04 Notes/{ARG}"
obsidian recents
```

Use the command that returns results. If neither matches, report and stop.

Record:
- The resolved folder root path
- The folder's name (last path segment) — this becomes the MOC title

---

## Step 2: Read all notes

Read every note returned by the Glob. For each note record:
- Its **subfolder** relative to the folder root (empty string if root-level)
- Its **frontmatter properties** (ignore `tags`)
- A **one-line description**: use the first non-empty sentence after a heading, or the first non-empty line of body content

---

## Step 3: Build Recent Activity

Use a **Dataview query** scoped to the resolved folder so the section stays live — no static table to maintain.

Build the **Recent Activity** section as a Dataview codeblock:

````
## Recent Activity

```dataview
TABLE
  choice(
    dur(date(now) - file.mtime).hours < 24,
    round(dur(date(now) - file.mtime).hours, 1) + " hours ago",
    choice(
      dur(date(now) - file.mtime).days < 7,
      round(dur(date(now) - file.mtime).days, 1) + " days ago",
      dateformat(file.mtime, "MMM dd")
    )
  ) as "Last Modified"
FROM "{FOLDER}"
WHERE file.name != "untitled"
SORT file.mtime DESC
LIMIT 10
```
````

Replace `{FOLDER}` with the resolved folder path (e.g. `04 Notes/<subfolder>`).

---

## Step 4: Build the Index

Choose a grouping strategy based on what the notes have:

**If subfolders exist** — group by subfolder:
- `###` per subfolder, `####` per nested subfolder
- Loose root-level notes (no subfolder) go as bullets at the top before any groups
- Order subfolders alphabetically; notes within each group alphabetically

**If no subfolders exist** — fall back to grouping by frontmatter property:
- Pick the property that appears in the most notes (e.g. `Device`)
- `###` per property name, `####` per property value
- Notes with no value for the chosen property go as loose bullets at the top before the groups
- Order property values alphabetically; notes within each group alphabetically

**If no subfolders and no common properties** — flat alphabetical bullet list, no headings.

All entries use: `- [[Note]] — description`

---

## Step 5: Write

Scaffold: `obsidian create path="05 Menus/MOC_{FOLDER_NAME}.md" template="MOC"`

Fill sections:
- **Purpose** — one sentence: what this folder contains and why it exists
- **Recent Activity** — the table from Step 3
- **Index** — as built in Step 4

Run in parallel: open the note with `obsidian open path="05 Menus/MOC_{FOLDER_NAME}.md"`

State the output path when done.
