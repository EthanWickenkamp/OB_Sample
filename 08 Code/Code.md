---
title: Code
tags: [index, code]
---

# Code

Tooling and technical reference notes, grouped by language or runtime. Each note is a living doc — install commands, verified workflows, gotchas, and links to the authoritative upstream docs. Notes here are what Claude reads when a task touches that toolchain.

## Organization

| Folder | What goes here |
| --- | --- |
| [[AI]] | Local models, agentic tools, vector/search engines, anything model-adjacent |
| [[Bash]] | Shell environment, terminals, core Unix tooling |
| [[Git]] | Git itself, GitHub, hosting options, repo setup |
| [[JavaScript]] | Node, Bun, nvm, JS/TS frameworks (Remotion, etc.) |
| [[Python]] | The `uv` venv, language-specific reference, key libraries |

## Current notes

- **AI** — [[qmd]]
- **Bash** — [[Git Bash]]
- **Git** — [[Git Setup]], [[Collaboration Repo]]
- **JavaScript** — [[Bun]], [[nvm]], [[Remotion]]
- **Python** — [[uv]]

## Conventions

- One note per tool. If a tool has multiple sub-concerns (install, config, workflows), keep them as headings in one note until it outgrows the file.
- Put the install command near the top. Future-you will look for it first.
- Link out to official docs rather than duplicating them. This folder is for the *vault-specific* way a tool is used, not a mirror of upstream.
- New language or runtime? Create a folder for it. Do not nest notes under an existing language unless the tool is a direct dependent (e.g., `Bun` under `JavaScript`).
