# Vault Organization and Menu System

> How the folder structure works and how to use MOC skills to create navigable menus.

## Folder Structure

```
00 Attachments/   — Pasted images and files (auto-organized by topic)
01 Inbox/         — Drop zone for processing with /inbox
02 Calendar/      — Daily notes (YYYY-MM-DD.md)
03 Sources/       — Unprocessed input: web pages, transcripts, PDFs
04 Notes/         — Main knowledge base (primary note location)
05 Menus/         — Maps of Content and navigation indexes
10 Claude/        — Claude configuration and commands
11 Config/        — Templates and vault settings
```

## Folder Purposes

| Folder | Purpose | When to Use |
|--------|---------|-------------|
| `01 Inbox/` | Temporary holding area | Raw notes, quick captures, unprocessed ideas |
| `02 Calendar/` | Time-based notes | Daily logs, scheduled events, time-blocked tasks |
| `03 Sources/` | External inputs | Web fetches, transcripts, PDFs to process |
| `04 Notes/` | Knowledge base | Curated, refined notes—the "real" content |
| `05 Menus/` | Navigation | Auto-generated indexes, MOCs, structure notes |

## Chunking Notes in 04 Notes/

The `04 Notes/` folder should contain focused, atomic notes. Chunk by:

### Topic
```
04 Notes/Programming/Python/
04 Notes/Programming/JavaScript/
04 Notes/Programming/Go/
```

### Area
```
04 Notes/Work/Projects/
04 Notes/Work/Meetings/
04 Notes/Work/Onboarding/
```

### Concept
```
04 Notes/Concepts/Context-Management.md
04 Notes/Concepts/Mental-Models.md
04 Notes/Concepts/Systems-Thinking.md
```

## Tagging Strategy

Tags live in note frontmatter and should be:

- **Descriptive** — `#python`, `#workflow`, `#project-alpha`
- **Hierarchical** — `#area/work`, `#type/reference`
- **Actionable** — `#todo`, `#in-progress`, `#review`

### Example Frontmatter

```yaml
---
tags: [concept, context-management, vault]
created: 2026-03-15
---

# Note Title
```

### Useful Tags

- `#concept` — Explanatory notes
- `#reference` — Reference material
- `#template` — Reusable templates
- `#inbox` — Needs processing
- `#wip` — Work in progress
- `#permanent` — Fully curated, don't delete

## Using /moc to Create Menus

The `/moc` skill auto-generates a Map of Content for any folder.

### How /moc Works

1. Run `/moc 04 Notes/Programming`
2. Creates `05 Menus/Programming.moc.md`
3. Contains auto-indexed list of all notes in that folder
4. Grouped by subfolder

### Menu Structure

```markdown
# Programming

## Python
- [[Note 1]]
- [[Note 2]]

## JavaScript
- [[Note 3]]
- [[Note 4]]
```

## Menu Types

### Auto-Generated (via /moc)
- Folder indexes
- Tag-based collections
- Recency-based lists

### Manual
- Curated topic introductions
- Project overviews
- Learning paths

## Workflow

1. **Create in 04 Notes/** — Write and develop your note
2. **Add tags** — Categorize in frontmatter
3. **Run /moc** — Auto-generate menu when folder grows
4. **Link from menus** — Menus point to notes; notes link back

## Example: Building a Menu

```
1. Create notes in 04 Notes/:
   - 04 Notes/Vault/Manual-Context.md
   - 04 Notes/Vault/Commands.md

2. Run /moc Vault

3. Result in 05 Menus/Vault.moc.md:
   ## Vault
   - [[Manual Context Control vs ChatGPT]]
   - [[Obsidian Command-Driven Context Management]]
```

## Linking Back

From a menu note, link back to the parent menu:

```markdown
← [[04 Notes/Vault/]] | [[05 Menus/Vault MOC]]
```

This creates bidirectional navigation.

---

See also:
- [[Chat Artifacts vs GPT Projects]] — Why manual control matters
- [[Obsidian Command-Driven Context Management]] — Command usage
- [[Obsidian Skills Starter Pack]] — Available skills