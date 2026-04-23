# Obsidian Skills Starter Pack

> The skills shipped in `10 CLAUDE/skills/` — what each one is for and how to extend them.

Skills are directories under `10 CLAUDE/skills/` (symlinked to `.claude/skills/`). Each has a `SKILL.md` with a YAML frontmatter block; Claude Code auto-loads the frontmatter and only reads the body when the skill is triggered. That means you can keep detailed references, scripts, and assets alongside the skill without bloating every session.

Slash commands live in `10 CLAUDE/commands/` and are covered separately in [[Obsidian Command-Driven Context Management]]. Skills are the heavier, reusable capabilities — file formats, external tools, longer reference docs — that commands and plain-English requests both pull from.

## Available Skills

| Skill | Purpose |
| --- | --- |
| `obsidian-cli` | Read, create, search, and manage notes, tasks, and properties through the Obsidian CLI. Also supports plugin/theme dev — reload plugins, run JS, capture errors, take screenshots, inspect the DOM. |
| `obsidian-markdown` | Write and edit Obsidian Flavored Markdown — wikilinks, embeds, callouts, properties, tags, all the vault-specific syntax. |
| `obsidian-bases` | Create and edit Obsidian `.base` files — database-style table and card views with filters, formulas, and summaries. |
| `json-canvas` | Create and edit `.canvas` files — nodes, edges, groups, connections. For mind maps, flowcharts, and visual canvases. |
| `excalidraw-diagram` | Build Excalidraw diagram JSON for workflows, architectures, and concept visualizations. |
| `defuddle` | Extract clean markdown from a web page via the Defuddle CLI. Use instead of WebFetch for articles, docs, and blog posts — strips nav and clutter, saves tokens. Skip for URLs that already end in `.md`. |
| `feeds` | RSS and iCal feed integrator — fetches RSS items into `01 Raw Sources/` and maintains iCal feed notes in `02 Calendar/`. Supports `rss`, `ical`, `all`, `list`, and `add <kind> <name> <url>`. |
| `banana` | AI image-generation Creative Director powered by Google Gemini Nano Banana. Handles text-to-image, image editing, multi-turn creative sessions, batch workflows, and brand presets. |

## Quick Reference by Purpose

### Content capture and cleanup
- `defuddle` — web pages → clean markdown
- `feeds` — RSS + iCal into the vault
- `obsidian-markdown` — write proper Obsidian notes

### Vault operations
- `obsidian-cli` — full vault operations from the command line
- `obsidian-bases` — database-style views over notes

### Visual and media
- `json-canvas` — canvases, mind maps, flowcharts
- `excalidraw-diagram` — architecture and concept diagrams
- `banana` — generated images and brand assets

### Plugin/theme dev
- `obsidian-cli` — reload plugins, run JS, inspect DOM

## How Skills Get Triggered

Skills fire automatically when the frontmatter `description` matches what you (or a command) are asking for. That description is the only thing Claude sees until the skill is chosen, so it doubles as the trigger prompt. Good descriptions name the concrete things users say — *"when the user mentions wikilinks, callouts, or frontmatter"* — rather than abstract capabilities.

You almost never invoke a skill by name. Write what you want in plain English or run a command, and the right skill loads itself.

## Where Skills Live

```
10 CLAUDE/skills/<name>/
  SKILL.md          — frontmatter + body, always read first
  references/       — optional deeper docs the body can point to
  scripts/          — optional helper scripts (uv, bash, etc.)
  assets/           — optional static files the skill produces or consumes
```

`10 CLAUDE/` is symlinked to `.claude/` so Obsidian sees the files and Claude Code sees the config. See the symlink section of [[Welcome]] if that link is broken.

## Customizing a Skill

The cheapest way to improve a skill is to run it, notice what was off, and edit `SKILL.md`. Two edit targets matter:

- **Frontmatter `description`** — tune when the skill fires. If it's not triggering on the phrasing you actually use, add those phrases here.
- **Body** — the instructions the model follows once triggered. Tighten steps, add an example, remove a detour that cost tokens without helping.

## Adding a New Skill

1. Create `10 CLAUDE/skills/<name>/SKILL.md` with frontmatter:

   ```yaml
   ---
   name: <skill-name>
   description: <what it does and when to trigger — be specific about user phrasing>
   allowed-tools: Bash, Read, Write, Edit
   ---
   ```

2. Write the body as you would brief a teammate: the goal, the steps, any gotchas. Keep it short — push reference material into a sibling file and link to it.
3. If the skill shells out, drop a helper script next to `SKILL.md` and reference it by relative path.
4. Test with a realistic user prompt. Adjust the `description` until the skill fires without having to name it.

## Finding More Skills

- [Claude Code docs](https://code.claude.com/docs) — official skill patterns.
- Anthropic skills repo on GitHub — reference implementations worth reading.
- Community Discord and GitHub share channels — vault-adjacent skills, clippers, importers.

Before adopting a community skill, open the `SKILL.md` and skim the body. Skills run with the tools they declare — know what you're giving them before you drop the folder in.

---

See also:
- [[Obsidian Command-Driven Context Management]] — slash commands that build on these skills
- [[Vault Organization and Menu System]] — where skill outputs land in the folder structure
