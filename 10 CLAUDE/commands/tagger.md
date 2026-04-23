---
name: tagger
description: Analyze vault tags and suggest improvements, then apply approved changes.
allowed-tools: Task, Bash, Read
---

Analyze vault tags and suggest improvements. No arguments needed.

### 1. Spawn the tagger agent

Use the Task tool to spawn the tagger-agent:
"Analyze all tags in the vault and return structured suggestions for improvement. Follow your agent definition."

### 2. Present suggestions to the user

Relay the agent's numbered suggestion list clearly.

### 3. Ask the user which to apply

Ask: "Which of these would you like to apply? You can say 'all', list numbers (e.g. '1, 3, 5'), or 'none'."

### 4. Apply approved changes

Use the Obsidian CLI for all tag operations — never edit frontmatter manually.

**Reading tags on a note:**
```bash
obsidian property:read name=tags file="<note>"
```

**Setting tags (replaces entire list — comma-separated for multiple):**
```bash
obsidian property:set name=tags value="<tag1>,<tag2>" type=list file="<note>"
```

**Removing the tags property entirely:**
```bash
obsidian property:remove name=tags file="<note>"
```

---

**RENAME** — find all notes with the old tag, swap it in each note's tag list:
```bash
obsidian tag name=<old-tag> verbose
```
For each note: read current tags with `property:read`, replace the old tag with the new one in the comma-separated list, then set:
```bash
obsidian property:set name=tags value="<updated,comma,list>" type=list file="<note>"
```

**MERGE** — same as rename: read tags, replace removed tag with kept tag, set.

**SPLIT** — read each note under the broad tag to determine the right subtag, then read its tags, swap the broad tag for the subtag, set.

**REMOVE** — read current tags, drop the target tag from the list, set. If it was the only tag, use `property:remove`.

**NEW** — read current tags (if any), append the new tag, set.

### 5. Confirm

Report what was changed: `tag changes applied to X notes`.
