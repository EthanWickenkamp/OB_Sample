---
name: sync
description: Pull and rebase latest vault changes from origin, handling dirty working tree automatically.
allowed-tools: Bash
---

Full vault sync: pull, commit, push — all automatic unless a conflict requires user input.

## Steps

1. Run `git fetch origin && git status` to see the current state.

2. **Pull phase** — if behind origin:
   - If there are uncommitted local changes: stash them first (`git stash`)
   - Run `git pull --rebase origin master`
   - If stashed: pop the stash (`git stash pop`)
   - If stash pop or rebase produces a merge conflict:
     - If the conflict is a **file deletion** or the diff shows **significant work being discarded**, stop and ask the user how to resolve.
     - Otherwise, resolve automatically (prefer the newer version), `git add` the resolved files, and continue the rebase.

3. **Commit phase** — if there are uncommitted local changes (modified, added, or deleted files):
   - Run `git add .`
   - Draft a concise commit message describing the actual changes (what notes were added, edited, reorganized). Be specific, one line, present tense. Do NOT use "vault backup:" — that's for the auto-plugin.
   - Commit without asking for confirmation.

4. **Push phase** — if there are unpushed commits:
   - Run `git push`

5. Report final state: up to date, short SHA, summary of what happened (pulled N commits, committed M files, pushed).
