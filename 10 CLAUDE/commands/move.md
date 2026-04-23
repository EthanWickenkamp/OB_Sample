---
description: Move or rename a note, auto-updating all wikilinks.
argument-hint: source path, destination path
allowed-tools: Bash
---

Move or rename a note. $ARGUMENTS: source path, destination path (describe naturally — Claude resolves vault-relative paths).

### 1. Move the file

```bash
obsidian move path="SOURCE_PATH" to="DEST_PATH"
```

### 2. Open at new location

```bash
obsidian open path="DEST_PATH"
```

### 3. Confirm

"Moved SOURCE → DEST"
