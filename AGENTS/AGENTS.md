# AGENTS.md

This file provides guidance to Pi coding agent when working in this Obsidian vault.

## Vault

This is an Obsidian vault — a folder of markdown files. You have full read access. Write access is restricted to `12 PI/` by default (enforced by the protected-paths extension). Request explicit permission before editing files outside that boundary.

## Obsidian CLI

Vault name: `OB_name`. Run Obsidian commands via bash:

```
obsidian open path=<path>
obsidian files folder=<path> ext=<ext>
obsidian recents
obsidian rename file=<name> name=<new>
obsidian delete file=<name>
obsidian property:set name=<n> value=<v> file=<f>
obsidian property:remove name=<n> file=<f>
```

Full reference: `config/Obsidian CLI Commands.md`

## Structure

- `00 Attachments/` — images and files
- `01 Raw Sources/` — unprocessed input, transcripts, clippings
- `02 Calendar/` — daily notes `YYYY-MM-DD.md`
- `04 Notes/` — ideas and projects (default location)
- `05 Menus/` — Maps of Content
- `06 Deliverables/` — finished outputs
- `08 Code/` — code reference notes
- `09 Classes/` — course content
- `10 CLAUDE/` — Claude Code config
- `11 GEMINI/` — Gemini CLI config
- `12 PI/` — Pi agent workspace (you write here)
- `config/Templates/` — note templates

## Agents

Specialized agents live in `12 PI/agents/`. Each has its own `AGENTS.md` that overrides this one when Pi is launched from that directory.

- `12 PI/agents/chat/` — general-purpose vault chat
- `12 PI/agents/vault-tools/` — link finding, orphan detection, tag audit
- `12 PI/agents/youtube-summary/` — structured video summaries

## Python

Venv at `~/.venvs/claude/`. Never use bare `python`.

```bash
"$HOME/.venvs/claude/Scripts/python.exe" -c "..."   # Windows
"$HOME/.venvs/claude/bin/python" -c "..."            # Linux
```
