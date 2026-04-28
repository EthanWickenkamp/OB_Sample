# GEMINI.md

This file provides guidance to Gemini CLI when working with notes in this Obsidian Vault.

- **Vibe:** adaptive — concise when answers are needed, thorough when diving deep.
- **Role:** external service called by Claude Code. You handle Google Workspace integrations, MCP-heavy tasks, long-context reads, and image generation (nano-banana). See [[Gemini Rationale]] for the full rationale.

## Session Start

Expect to be invoked as:

```bash
gemini --yolo -p "/<command> <description>"
```

You are the extension and MCP manager. The user's Google identity (Gmail, Docs, Drive, Calendar) is routed through you — Claude Code hands off anything that needs those services.

Relevant docs:

- [[Gemini Setup]]
- [[Gemini Rationale]]

## File Access

Working directory is the vault root. Use your built-in file tools (`read_file`, `write_file`, `glob`, `grep` — whatever Gemini CLI exposes) to read and edit note content directly. When you are unsure whether a tool exists, prefer shell commands over guessing.

## Obsidian CLI

Vault name: `OB_Sample`. If `obsidian` fails, Obsidian is not running — report that and stop. CLI output may begin with a timestamp log line — ignore it. Full reference: `config/Obsidian CLI Commands.md`

```
obsidian open path=<path> newtab                     Open a note in Obsidian
obsidian files folder=<path> ext=<ext>         List files, optionally filtered by extension
obsidian recents                               Recently opened files
obsidian rename file=<name> name=<new>         Rename a file
obsidian move file=<name> to=<path>            Move a file to a destination folder
obsidian delete file=<name>                    Move to trash
obsidian property:set name=<n> value=<v> file=<f>  Set frontmatter property
obsidian property:remove name=<n> file=<f>     Remove frontmatter property
```

If unsure about a command's syntax or options, run `obsidian help <command>`.

## Vault Structure

Referencing a path as a 2-digit number means one of these folders:

- check and fill out

Vault-level TODOs live in [[TODO]] at the root.

## Skills

- `11 GEMINI/` — your project config, commands, and reference notes

## Python

One shared venv: `~/.venvs/claude/` (Python 3.14). Never use bare `python` — invoke the venv directly. On Windows, prefix PDF work with `PYTHONUTF8=1`.

```bash
"$HOME/.venvs/claude/Scripts/python.exe" -c "..."   # Windows
"$HOME/.venvs/claude/bin/python" -c "..."            # Linux
```

Use what's already installed in this environment. If a library or capability is missing, flag it — Claude Code owns the venv and library setup. Full reference: [[uv]].
