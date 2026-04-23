---
description: Analyze a folder for stale, duplicate, or overlapping notes — merge or remove them with user approval.
argument-hint: folder path or name
allowed-tools: Bash, Read, Write, Edit, Glob, Grep, AskUserQuestion
---

Analyze `$ARGUMENTS` (a folder path or name likely under `04 Ideas/`) for notes that are empty, stale, orphaned, or redundant.

1. Glob all `.md` files in the folder. Run `obsidian outline` on each to get heading structure without reading full content.
2. Grep across the folder for repeated terms, shared headings, or overlapping topic keywords to surface likely duplicates.
3. Read any notes that look like candidates based on outline + grep. Flag:
   - **Empty** — little or no content
   - **Overlap/duplicate** — same topic covered in multiple notes; suggest merge
   - **Outdated/contradicted** — content that conflicts with or is superseded by another note; suggest update or removal
   - **Upgradeable** — a stub or rough draft that could be promoted to a fuller note or Crystal
4. Present a short report grouped by flag type with a suggested action for each (merge into X, delete, upgrade, keep).
5. Act on user decisions. Always confirm before any destructive action.
