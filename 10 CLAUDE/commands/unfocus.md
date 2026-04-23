---
name: unfocus
description: Close a focus session — review what was done, ask confirming questions about system layout and decisions, update the session log.
allowed-tools: Bash, Read, Edit, Glob
---

Close the current focus session. No arguments.

---

## Step 1: Find the active session

Read today's daily note:
```bash
obsidian daily:read
```

Find the `## Focus Sessions` section. Locate the last `###` entry — this is the active session.

Extract the MOC name from the `**MOC:**` field and read it:
```bash
obsidian read file="<MOC name>"
```

If there is no Focus Sessions section or no entries, say: "No active focus session found today."

---

## Step 2: Review what happened

Read the `**Activity:**` lines from the session log. Also check git for changes made during the session:
```bash
git diff --name-only
git diff --cached --name-only
```

Cross-reference the activity log with actual file changes to build a complete picture of what was done.

---

## Step 3: Ask confirming questions

Based on the work done during the session, ask 2-3 targeted questions that probe whether the system layout, architecture, or decisions captured in the notes are accurate. Focus on:

- **Structural accuracy** — "We wrote that X connects to Y — is that how it actually works?"
- **Completeness** — "We didn't cover Z — is that intentional or a gap?"
- **Decision confirmation** — "We settled on approach A — is that locked in or still open?"

These questions should reflect genuine understanding of the domain, not generic prompts. Read the relevant notes to inform the questions.

Wait for user responses.

---

## Step 4: Update the session log

After the user answers, append to the activity log:
```
- {HH:MM} — Session closed
```

If the user's answers revealed corrections or new information, note them:
```
- {HH:MM} — Confirmed: {confirmed decision or fact}
```

---

## Step 5: Update the MOC if needed

Re-read the MOC (`obsidian read file="<MOC name>"`). If during the session:
- New notes were created — add their wikilinks to the appropriate section
- Notes were renamed or moved — update the links
- Coverage gaps were addressed — remove them from the gaps list

Only modify the MOC if there are actual changes to reflect. Show the user what you're updating before writing.
