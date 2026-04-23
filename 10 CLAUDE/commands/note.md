---
description: Load, create, or open a note by name or path.
argument-hint: "[create] note name or path [template=name]"
allowed-tools: Bash, Read, Glob, Edit
---

Note operations. Route by $ARGUMENTS:

| Pattern                       | Action                                  |
| ----------------------------- | --------------------------------------- |
| `create path [template=name]` | Create a note from template and open it |

## create path [template=name]

Create a new note and open it in Obsidian.

```bash
obsidian create path="<dest>" template="<template name>" open
```

If no template specified, create with empty content. Templates are in `config/Templates/` (core Templates plugin). Read the template first if you haven't seen it before.

Available templates: `obsidian templates`
