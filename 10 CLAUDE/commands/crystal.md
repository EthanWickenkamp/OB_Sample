---
description: Promote a tag or note to a Crystal — a curated, distilled knowledge note in 05 Menus/.
argument-hint: tag name | note title/path
allowed-tools: Bash, Read, Write, Edit
---

Promote a tag or note to a Crystal. $ARGUMENTS: tag name or note title/path.

A Crystal is a curated, distilled knowledge note — editorially chosen links, prose overview, a living summary of what you know about a topic. Unlike an auto-generated MOC, a Crystal is where *you* bring structure and ideas to a hub.

> For folder indexing (auto-index of all notes in a folder), use `/moc` instead.

---

## Step 1: Resolve argument

Run in parallel: `obsidian tags counts sort=count` and `obsidian recents`.

Filter `.tmp` files from recents output — these are editor artifacts.

Match argument (case-insensitive, strip `#`):
- **TAG** — found in tags list → `obsidian tag name={TAG} verbose`
- **NOTE** — use CLI name resolution: `obsidian read file="<argument>"`

If the argument looks like a folder path, stop and say: "This looks like a folder — use `/moc` to generate a Map of Content for it."

---

## Step 2: Gather and read notes

For TAG: read a representative sample of the returned notes using `obsidian read file="<name>"`.
For NOTE: read that one note (already resolved in Step 1).

**STRICT: Only index notes from the source list.** Notes merely mentioned inside other notes do not belong in the Index.

---

## Step 3: Build the Index

For each note, record:
- Its **frontmatter properties** via `obsidian properties file="<name>" format=yaml` (ignore `tags`)
- Whether it's **loose** (no non-tag properties, or single note source)

Then build the Index in this order:

**1. Loose notes** — bullets at the top (no heading)
- `- [[Note]] — description`

**2. Property groups** — one `###` per property name, one `####` per value
- Process properties in the order they first appear across the note set

If there are no property groups, use `####` for all groups (no `###` level).

---

## Step 4: Write

Scaffold: `obsidian create path="05 Menus/◇_{NAME}.md" template="Crystal"`

Fill sections:
- **Overview** — 1–3 sentences: what this topic is, why it matters, current state
- **Recently** — wikilinks to notes also in `obsidian recents`. Omit if none.
- **Index** — as built above

Open: `obsidian open path="05 Menus/◇_{NAME}.md"`

**Note branch only:** ask "Delete the original at {SOURCE_PATH}?"

State the output path when done.
