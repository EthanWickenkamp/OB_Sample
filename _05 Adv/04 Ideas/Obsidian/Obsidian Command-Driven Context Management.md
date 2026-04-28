# Obsidian Command-Driven Context Management

> How to use vault commands to manually load, navigate, and control the context bank.

Claude Code commands are just `.md` files in `10 CLAUDE/commands/` (mapped to `.claude/commands`). Each one is a tiny prompt with a frontmatter block declaring its allowed tools. That means they are cheap to add, cheap to edit, and you are never stuck with the ones shipped in the template.

A command is a quick, deterministic **hook** — a little prompt plug-in you drop into the conversation to get a specific, repeatable output from the agent. Each one is flat: a short set of steps the model runs against the vault or the Obsidian CLI. Call it with `/name`, or just say the word in a sentence and the agent catches the hook. Most of the ones below are for navigating context and doing routine vault/Obsidian work.

## Core Commands

The everyday, low-effort ones. Run them whenever you need the vault to hand you a specific thing.

| Command | What it does |
| --- | --- |
| `/current` | Load the note currently open in Obsidian into context. |
| `/daily` | Daily note hub — view today, add a to-do, add an event, show upcoming. Subcommands: `/daily todo …`, `/daily event …`, `/daily upcoming`. |
| `/note <title>` | Load, create, or open a note by name or path. `/note create <title> [template=…]` to create. |
| `/search-context <query>` | Full-text search plus tags, links, backlinks, outlines, orphans, and unresolved links — the main exploration command. |
| `/pickup` | Summarize recent vault activity so you can figure out where you left off. |
| `/move <src> <dst>` | Move or rename a note, preserving all wikilinks. |
| `/sync` | Pull, rebase, and push vault changes against the git remote. Handles a dirty working tree. |
| `/youtube-transcript <url>` | Fetch a YouTube transcript and save it into `01 Raw Sources/`. |

## Workflow Commands

Bigger, concept-level commands. These shape the vault itself — building hubs, processing captures, running longer sessions. Each one does several steps and usually writes or rewrites notes.

| Command | What it does |
| --- | --- |
| `/moc <folder>` | Generate a Map of Content for a folder — an automatic, complete index grouped by subfolder. Stored in `05 Crystal/`. Use this for structure. |
| `/crystal <tag or note>` | Promote a tag or note to a Crystal — a curated, editorial hub with prose and hand-picked links. Use this when *you* bring the structure. |
| `/focus <MOC>` | Start a deep-work session on a MOC: load all linked notes, pin a session log to today's daily note. |
| `/unfocus` | Close the current focus session — review what changed, update the session log, ask a few confirming questions about decisions made. |
| `/inbox` | Process and organize whatever landed in `Inbox/`. Spawns a dedicated agent. |
| `/tagger` | Analyze the vault's tags and propose consolidations, renames, or deletions before applying approved changes. |

## Experimental Commands

These work, but the shape of the prompt is still being tuned. Run them, see what you get, tell Claude what you wanted instead, and rewrite the command file. That loop is how a command graduates into the core set. More of these at [[Obsidian Commands 1]] by [InternetVin](https://internetvin.com/Obsidian+Commands)

| Command                                      | What it does                                                                                                                                             |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/synthesize <notes or folder> [> question]` | Read a set of notes and write the densest paragraph(s) that capture the thesis, then reflect on structure.                                               |
| `/prune <folder>`                            | Analyze a folder for stale, duplicate, or overlapping notes and walk through merges/removals with approval.                                              |
| `/to-sample <path>`                          | Generalize one of your reference notes or commands into a template-worthy version for `OB_Sample` — strips personal state, rewrites paths, softens tone. |
|                                              |                                                                                                                                                          |

## Context Loading Pattern

Instead of relying on the model's memory of earlier turns, load what matters each time:

```
/current                 → the note I'm looking at right now
/daily                   → today's tasks and events
/note <title>            → a specific reference note
/search-context <query>  → surface relevant notes before acting
/focus <MOC>             → a whole topic with its linked notes
```

Every load is a deliberate "put this on the table." When you're done with a piece of context, don't reload it.

## Principles

1. **Explicit over implicit** — load exactly what you need.
2. **Command-first** — if you do it twice, consider a command.
3. **Context bank** — notes are the bank; commands are the withdrawals.
4. **No auto-loading** — you decide what persists in context.

## Anti-Patterns to Avoid

- Letting the AI auto-crawl the vault without a prompt.
- Creating commands that don't map to a real, repeated workflow.
- Over-automation — sometimes one-off natural language is faster than a command.
- Hoarding experimental commands that never graduate. Cut what you don't use.

## Growing the Command Set

### Adding a new command

1. **Identify the pattern** — what repeated action are you doing?
2. **Check the tools it needs** — `Bash`, `Read`, `Edit`, `Write`, `Glob`, `Grep`, `Task`, or a specific skill.
3. **Create the file** — `10 CLAUDE/commands/<name>.md` with frontmatter:

   ```yaml
   ---
   name: <name>
   description: <one line — this is what shows up in /help>
   argument-hint: "<shape of arguments>"
   allowed-tools: Bash, Read, Edit
   ---
   ```

4. **Write the prompt** — short, imperative, reference `$ARGUMENTS` where input is expected.
5. **Iterate** — run it, note what went wrong, edit the file, run again.

### Candidate commands to add

- **Quick capture** — jot a thought into `Inbox/` with a timestamp, then route it later with `/inbox`.
- **Weekly review** — load the last 7 daily notes and summarize open todos.
- **Backlinks explorer** — for the current note, list incoming links with surrounding context.
- **Tag cloud** — visual overview of the current tag structure, overlap with `/tagger`.

## Integration With Artifacts

These commands feed the broader [[Chat Artifacts vs GPT Projects]] system:
- Commands load notes → notes become artifacts → artifacts build refined context.
- Each loaded note is a reprompt opportunity — rewrite it based on what the model got wrong.
- Daily notes capture work; reference notes and Crystals provide facts and taste. Wiki gathers references for ideas.

---

See also:
- [[Vault Organization and Menu System Old]] — folder structure and menus
- [[Obsidian Skills Starter Pack]] — the skills these commands lean on
