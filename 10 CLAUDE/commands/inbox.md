---
name: inbox
description: Process and organize notes dropped in Inbox/.
allowed-tools: Task
---

Process notes in `Inbox/`. No arguments needed.

Spawn the inbox agent using the Task tool:

```
Use the Task tool to spawn the inbox-agent. Pass this instruction:
"Process all notes in Inbox/ — assign tags and move each to the correct vault location. Follow the steps in your agent definition."
```

Wait for the agent to finish, then relay its report to the user.
