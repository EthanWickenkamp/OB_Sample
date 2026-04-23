---
title: Workspaces
tags: [index, workspaces]
---

# Workspaces

A workspace is a self-contained project directory that holds everything a single recurring kind of work needs: code, context, drafts, references. Each one has its own `CLAUDE.md` at the root that tells Claude how to behave inside it — the routing table, naming conventions, and rules specific to that project.

## How a workspace is structured

```
<Workspace>/
├── CLAUDE.md          ← Orientation: purpose, routing, rules, conventions
├── <subfolder>/       ← Phase or concern (planning, src, drafts, renders)
│   └── CONTEXT.md     ← Deeper context for that subfolder (optional)
└── ...
```

Claude reads the workspace `CLAUDE.md` on entry. Subfolder `CONTEXT.md` files are loaded on demand based on the routing table.

## Current workspaces

| Workspace                                                       | Purpose                                                                    |
| --------------------------------------------------------------- | -------------------------------------------------------------------------- |
| [[_05 Adv/07 Workspaces/NanoBanana/CLAUDE\|NanoBanana]]                               | AI image generation via Gemini + banana skill                              |
| [[_05 Adv/07 Workspaces/NotebookLM/CLAUDE\|NotebookLM]]                               | Source-heavy research via Google NotebookLM, distilled back into the vault |
| [[_05 Adv/07 Workspaces/REMOTION/CLAUDE\|REMOTION]]                                   | Data-driven video production with Remotion (React + TS)                    |
| [[Content Directory Structure\|MWP]]                                | Reference material and workflow starter docs (not a live workspace)        |

## Creating a new workspace

1. Copy the closest existing workspace as a starting point.
2. Edit its `CLAUDE.md` — replace placeholder text, update the routing table, set naming conventions.
3. Add subfolders for each phase of the work, with a `CONTEXT.md` if that phase needs its own rules.
4. Add the workspace to the table above.

## Rules

- Workspaces are isolated. Never cross-reference files between workspaces unless explicitly asked.
- If a task doesn't belong to a workspace, it lives in `04 Notes/`, not here.
- Keep `CLAUDE.md` files tight — they are read on every entry. Push detail into `CONTEXT.md` or reference notes.
