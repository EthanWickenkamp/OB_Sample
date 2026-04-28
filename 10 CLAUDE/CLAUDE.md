# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with notes in this Obsidian Vault.

- **Vibe:** adaptive — concise when answers are needed, thorough when diving deep.
- **Output**: Answer questions in terminal respond, but be ready to write to the working note.
- **User:** [One sentence about who you are and what you use this vault for — replace this line.]

## Session Start

This vault is capable of being shared across multiple devices and backed by git. Sync from the remote at the start of every session before doing anything else. If git is configured otherwise, point at the relevant setup note in [[08 Code/Git/Git Setup]].

## File Access

The working directory is the vault root (`..\OB\OB_Sample`). Use the Read, Edit, Write, Glob, and Grep tools directly for reading and editing note content.

## Obsidian CLI

Vault name: `OB_Sample`. If `obsidian` fails, Obsidian is not running — report that and stop. Full reference: `config/Obsidian CLI Commands.md`

```
obsidian open path=<path> newtab               Open a note in Obsidian
obsidian file                                  Currently active note
obsidian files folder=<path> ext=<ext>         List files, optionally filtered by extension
obsidian outline file=<name>                   Heading structure of a note (peek without reading full file)
obsidian recents                               Recently opened files
obsidian rename file=<name> name=<new>         Rename a file (preserve links)
obsidian delete file=<name>                    Move to trash
```

Use `outline` to scan a note you are *not* opening. For the currently active note, run `obsidian file` to get the path, then Read the whole thing directly.

If unsure about a command's syntax or options, run `obsidian help <command>`.

## Vault Structure
**FIX for current layout**
Referencing a path as a 2-digit number means one of these folders:

- `00 Attachments/` — pasted images and files, topic-organized, plugin.
- `01 Raw Sources/` — Source material: web pages, PDFs, YouTube transcripts, clippings
- `02 Calendar/` — daily notes named `YYYY-MM-DD.md`
- `03 Wiki/` — distilled, stable reference layer. See [[WIKI]]
- `04 Notes/` — ideas, drafts, working project notes; default note location
- `05 Menus/` — Maps of Content and navigation notes. See [[MENUS]]
- `07 Workspaces/` — self-contained project directories, each with its own `CLAUDE.md`. See [[Workspaces]]
- `08 Code/` — tooling and technical reference, grouped by language/runtime. See [[08 Code/Code]]
- `10 CLAUDE/` — this directory. Claude Code project config (commands, skills, agents)
- `11 GEMINI/` — Gemini CLI project config and reference
- `12 PI/` — Pi coding agent directory (agents, prompts, extensions)
- `Clippings/` — saved web clippings (unnumbered, Obsidian-managed)
- `config/` — vault management: `Templates/`, `Scripts/`, `Icons/`, plugin notes

Vault-level TODOs and lookover items live in [[TODO]] at the root.
Vault user navigation panel at HOME at the root.
## Workspaces

When entering a `07 Workspaces/<name>/` directory, read that workspace's `CLAUDE.md` first — it has the routing table, conventions, and rules for that project. Consider using agents for a specific workspace task.

## Skills

- `10 CLAUDE/commands/` — flat `.md` files for slash commands, simple CLI steps
- `10 CLAUDE/skills/` — directories with `SKILL.md` for shared skills that have supporting files (references, scripts, assets)
- `10 CLAUDE/agents/` — subagent definitions

## Python

One venv: `~/.venvs/claude/` (Python 3.14). Never use bare `python` — invoke the venv directly. On Windows, prefix PDF work with `PYTHONUTF8=1`.

```bash
"$HOME/.venvs/claude/Scripts/python.exe" -c "..."   # Windows
"$HOME/.venvs/claude/bin/python" -c "..."            # Linux
```

**Available libraries:** `youtube-transcript-api`, `pymupdf4llm`, `python-doctr`, `matplotlib`, `openpyxl`, `pandas`, `python-docx`, `beautifulsoup4`, `pypandoc_binary`, `python-pptx`, `python-frontmatter`, `pillow`, `httpx`, `markdownify`, `tiktoken`, `pdfplumber`, `yt-dlp`

Full reference, verification checklist, and rebuild instructions: [[08 Code/Python/uv]].
