---
name: reconcile
description: Evaluate the structure of one or more idea spaces and reorganize them — the spatial counterpart to /synthesize. Supersedes /prune (in-folder hygiene).
argument-hint: "path[|path…] [> focus question]"
allowed-tools: Bash, Read, Glob, Grep, Edit, AskUserQuestion
---

Evaluate the structure of one or more idea spaces and reorganize them. The counterpart to `/synthesize`: synthesize collapses *content* into a thesis; **reconcile arranges *notes* into a structure** (semantic vs. spatial). Supersedes `/prune` (in-folder hygiene) — this diagnoses both within and across spaces, then acts.

`$ARGUMENTS`: one or more folder paths or note names separated by `|` (or newlines), optionally followed by `> focus question`. One space = internal-structure + hygiene mode. Multiple = cross-space relationship + restructure mode.

Think before acting. Diagnose the whole picture before moving a single file.

---

## Step 1: Parse arguments

Split on `>` for an optional **focus**. Split the left side on `|` (or newlines) into one or more **paths**. Trim each.

If a path doesn't resolve as a folder (Glob `{path}/**/*.md` and `04 Notes/{path}/**/*.md` both empty), treat it as a note name. If nothing resolves, report and stop.

---

## Step 2: Gather + classify

For each space, Glob its `.md` notes (read all, or ~12 most-recently-modified per space if large). Also `find "{path}" -type f` once — **`.md` globs miss `.excalidraw`/`.svg`/attachments**; you'll need the full file list before any move or delete.

Per note, collect in parallel:
- **Words:** `obsidian wordcount file="<name>" words`
- **Backlinks:** `obsidian backlinks file="<name>" total`
- **Last commit:** `git log -1 --format="%ai" -- "<FILE>"`
- **Type:** frontmatter `tags: clippings` + a `source:` URL = external **clipping**; else **authored**
- First heading + first body line (from Read) for context

Once for vault context: `obsidian orphans`, `obsidian deadends`.

**Also check for an existing index:** Glob `05 Menus/MOC_*{space}*`. A folder's MOC must be reconciled too when the folder changes.

---

## Step 3: Diagnose structure

Build a compact concept map per space (internal — not output). Then classify, at both the note and the space level:

| Relationship | Meaning | Default action |
|---|---|---|
| **Load-bearing** | the spine other notes orbit | keep central; make it the hub |
| **Complementary** | different angle, each earns its place | keep both; cross-link |
| **Superseded** | a newer/fuller note replaces an older one | **archive** the old (salvage durable bits first) |
| **Duplicate** | the same thing twice | **merge** → prune |
| **Stub / stale / orphan** | <20 words, no commits in 120d, or no links | **prune** or fold in |
| **Misfiled** | a clipping among notes, or a service note in a philosophy folder | **restructure** (re-home) |

When spaces relate as a **maturity / provenance chain** (one grew out of another, one supersedes another), say so explicitly and name which is the living layer — that ordering drives the whole restructure. If they stack as layers, draw a short ASCII stack/provenance diagram.

---

## Step 4: Present the reconcile report

```
## Reconcile: {SPACES}

{structure view — stack/provenance diagram or one-line-per-space}

### Relationships
- **[type]** — {note/space} ↔ {note/space}: one sentence + why it matters

### Proposed actions
| Cluster | Verdict | Action | Lands at |
|---------|---------|--------|----------|
| ...     | superseded / duplicate / stub / misfiled | merge / prune / archive / restructure | path |

### Quick wins
{exact dups, empty stubs, obvious misfiles — low-judgment}
```

Omit empty sections.

---

## Step 5: Decide the forks

For anything beyond an obvious quick win — where notes land, merge-vs-archive, the target shape — **use AskUserQuestion** rather than guessing. Moving many files the wrong way is expensive to redo. Get the structure confirmed before touching files.

---

## Step 6: Apply — safely

**Moves go through `obsidian move path=… to=…`, never `git mv`/`mv`.** It auto-rewrites *every* wikilink form, including path-qualified ones (`[[04 Notes/X/Y]]`). Plain moves silently break those. Folders can't move as a unit — move files individually; `mkdir -p` the destinations first.

- **Merge:** read source + target; append the source's unique content under `## Merged from [[Source]]`; repoint backlinks (`Grep` → `Edit`); delete the source.
- **Archive:** relocate into an archive subfolder (keep, demote) rather than delete, when the content is dated-but-worth-keeping.
- **Prune:** check backlinks first; `obsidian delete file="<name>"` (trash, recoverable). Confirm before each destructive action — never batch-delete without per-note/per-group approval.
- **Restructure:** re-home misfiled notes; clippings → a `Sources/` subfolder, authored notes by topic.

**`obsidian move` does NOT touch — fix these by hand after:**
1. Dataview `FROM "old/path"` strings (code) → update to the new path.
2. Links to *deleted* files → repoint to the surviving equivalent.
3. The folder's `MOC_` note → fix FROM path, dead links, add a relocation banner; update the destination's index too.

Then verify: `obsidian unresolved verbose` — filter to the moved/deleted names to ignore pre-existing breakage.

---

## Step 7: Summary

```
## Reconcile complete

- Merged: {N}   Pruned: {N}   Archived: {N}   Restructured: {N}
- MOCs updated: {list}
- Links repaired: {N}   Unresolved (mine): 0
```
