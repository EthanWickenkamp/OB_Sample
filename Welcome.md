# Welcome to Your Vault

This vault is a local, plain-text knowledge system built on two things working together:

- **Obsidian** — the editor/viewer. Browse, link, and visually work with your notes.
- **Claude Code** — the engine. It searches the vault, creates structure, runs skills, and handles the repetitive maintenance parts so you can focus on thinking. 
*Claude Code is the best out of the box harness but a custom PI harness is likely ideal.*

## What is Obsidian

Every note is just Markdown. You own the files, the links, and the structure — which means everything the AI creates and uses stays entirely visible and easily editable. Markdown is a native text output of AI like code. The usual chat interfaces output and display in Markdown. Instead of chats trapped in project folders in ChatGPT, here we are managing chat artifacts that are iterated on to provide refined context to any session.

> [!tip] Basic Obsidian Usage
> Think of this as a notebook that can cross-link itself. When you type `[[Like This]]`, you are linking one note to another. Over time, those links turn a pile of notes into a knowledge graph. The knowledge graph is essential to fully utilizing the current and future AI improvements. Try `shift+tab` hotkey or open the graph view near the top of the left sidebar.

## How to think about this vault

The vault is the **scaffolding** — the folders, templates, skills, and notes that give structure to your work. Claude Code is the **engine** that runs the LLM inside it.

The goal is to allow anyone programming background or not to experience the full capabilities of frontier coding agents and build an agent harness. Obsidian is essentially an IDE for English markdown.

It is also important because this is essential to utilizing the capabilities of newer models. At the core this vault is just md text files. You own and control your harness scaffolding of context and instructions as a folder of files on your computer.  The vault gets vastly more powerful as you add to it and shape it. This happens primarily in **3** ways.

#### 1. Raw Sources
Information collected as web clippings (Obsidian browser extension), PDFs, docs, pptx, YouTube video transcripts, Images, RSS/other feeds. Any research or material related to what you are working on or learning — dump it in.

#### 2. Distilled Knowledge
Your work, synthesis, and distilled knowledge. The content you create gives personal and domain-specific context that Claude can use. The wiki of references attempts to build and manage itself through agents relating raw sources with your findings and decisions.

#### 3. Skills and Agents
Claude skills, agents, and automations. As you work, think of tasks and prompts that create useful outputs from Claude. This includes scheduled agents and potential [[n8n]] integration. Create code and tie in more CLI command tools Claude can run in skills. The easy foundation for this is the [[uv|uv]] Python venv.

#### Compounding
Every source you add, note you write, link you make, and skill you save compounds. This principle remains true regardless of advancements in AI. A smarter or cheaper model from any provider can be plugged in as the engine powering your scaffolding. A Markdown file is the simplest shared layer between humans and LLMs — just a text file.

#### Two small habits to keep in mind as you go:

- **Distill, don't dump.** Raw captures are fine — `Inbox/` and `01 Raw Sources/` exist for exactly that. But the real value shows up when you rewrite, link, and shape rough material into notes that apply to your work and learning.
- **Skills grow with you.** Most Claude commands (`/note`, `/daily`, `/moc`) are just Markdown files in the vault. When Claude does something impressive or a session is particularly productive, ask it to draft a skill or agent from it. If a skill is unreliable or lacking, run through it once or twice and tell Claude to log successful steps and rewrite it at the end with your suggestions.

## Before You Start — Setup Checklist

This vault is designed to be used with **Obsidian** (for browsing) and **Claude Code** (for editing, creating, and organizing). If you're setting up from scratch, work through these in order. Each step links to a website or note in `08 Code/` or `config/` with full instructions.

### 1. Install Obsidian

Download from [obsidian.md](https://obsidian.md), then open this folder as a vault: **File → Open vault → "Open folder as vault" → pick this folder**.

### 2. Install a Unix-style terminal (optional but recommended)

On **Windows**, install [[Git Bash]] from [git-scm.com](https://git-scm.com). On **Mac/Linux**, your built-in Terminal already works. Commands in the rest of this vault can assume a Unix-style shell.

### 3. Install Node.js via nvm

Claude Code runs on Node. [[nvm]] keeps Node installs clean and lets you upgrade, reinstall, change versions, without breaking things.


### 4. Install Claude Code

One `npm install -g` command, then run `claude` inside this folder and sign in with your Anthropic account. See [Quickstart - Claude Code Docs](https://code.claude.com/docs/en/quickstart) for the full install and first-run walkthrough.
Bash: `curl -fsSL https://claude.ai/install.sh | bash`
powershell: `irm https://claude.ai/install.ps1 | iex`

### 5. Symlink `10 CLAUDE/` ↔ `.claude/`

Claude Code looks for project commands, agents, and settings in `.claude/` at the working directory. This vault keeps them in `10 CLAUDE/` so they show up in Obsidian's file tree. Link the two so edits in one are visible to both. To do this delete any existing `.claude` folder in the vault and make a system level link, this will duplicate `10 CLAUDE` to `.claude`.

**Windows (cmd, run as administrator):**
```bash
cd /c/path/to/OB_Sample
mklink /D ".claude" "10 CLAUDE"
```

**Mac/Linux:**
```bash
cd /path/to/OB_Sample
ln -s "10 CLAUDE" .claude
```

Full walkthrough and troubleshooting in [[Symlink Setup]].

### 6. Obsidian Terminal Plugin

**How it works, in basic terms.** The plugin adds a pane inside Obsidian that runs a real shell as a child process, so you can type commands next to your notes instead of Alt-Tabbing to a separate terminal. The flow is:

`Obsidian` → `Terminal plugin` → `shell (Git Bash / cmd / zsh)` → `claude` CLI

A **profile** is just a pointer to a shell executable plus its arguments. You pick one from the dropdown when opening a terminal. The vault ships with a Git Bash profile (`win32GitBash`) pre-configured in `.obsidian/plugins/terminal/data.json`, pointing at the default Windows Git install path (`C:\Program Files\Git\bin\bash.exe`). Make it the default by setting `defaultProfile` to `win32GitBash` in that same file. The other built-in profiles (`win32IntegratedDefault`, etc.) fall back to `cmd.exe`.

Enable from **Settings → Community plugins**, then open a terminal via the ribbon icon or command palette (**Terminal: Open terminal**). Inside that terminal, type `claude` to start Claude Code.

> [!warning] Rendering and spawn caveats
> The embedded terminal is a JavaScript emulator (xterm.js) running inside Obsidian's Electron window — not a full native terminal. Expect rough edges:
> - **Glyphs and prompt decorations** (powerline icons, nerd-font symbols, emoji) can display slightly off or as boxes.
> - **Resize is laggy.** You may see `error spawning terminal resizer` — Claude Code tries to launch a helper to track pane size and the plugin's sandbox sometimes blocks it. Harmless, but the UI may not reflow cleanly when you drag the pane.
> - **`spawn python3 ENOENT`.** On Windows, Python installs as `python.exe` or `py.exe`, not `python3`. Anything (a skill, a hook) that shells out to `python3` will fail here. Fix options: (a) install via [[uv]] and call `uv run python ...`, (b) alias `python3` to `py -3` in your Git Bash rc, or (c) add a `python3.exe` shim on PATH.
> - **PATH is inherited from Obsidian**, not your full login shell — tools you only installed into a specific shell's rc may not resolve. Launch Obsidian from a shell where your PATH is already correct, or hard-code absolute paths in profiles.
>
> For anything long-running or visually important (TUIs, `claude` sessions with rich output), prefer the native Windows Terminal or Ghostty profiles below.

### 6. (Windows) Configure Windows Terminal

Install the Microsoft **Windows Terminal** app from the Microsoft Store or likely already installed. 
Navigate to the vault `cd`, `ls`, `dir`, and you can launch [[ClaudeCode]] with `claude`
#### Custom Profile
We can make a custom Git Bash, Obsidian Vault, and Claude Code profile. Set the name, set the command line to `C:/Program Files/Git/bin/bash.exe -i -l -c "claude; exec bash"` this uses git bash and runs `claude` command. Then set starting directory to the vault ex: `%USERPROFILE%/OB/Vault1`. Finally at `/config/icons` in this vault there are a few icons of clawd or make an icon with [[NanoBanana]]. You can also turn this into a desktop shortcut by creating a new shortcut and using the target `wt.exe -p "Profile Name"` Full walkthrough and json profile example to ctrl-v the profile at [[Windows Terminal]].

### 6. (Mac/Linux) Install Ghostty
[Ghostty](https://ghostty.org/)
[[Ghostty]] is a fast, modern terminal emulator with cleaner rendering and better defaults than the built-in options. It is a drop-in replacement for macOS Terminal. Optional, but very useful if you ever plan to run multiple agent tabs or want to customize your terminal. Recommended by ClaudeCode creator, no windows version.

### 7. (Optional) Version your vault with git
Turn this folder into a git repository so every change is stored, and so you can sync the vault across devices. See [[Git Setup]] for three options (local-only, self-hosted server, or private GitHub repository).

### 8. Install Python via uv
[Installation | uv](https://docs.astral.sh/uv/getting-started/installation/)
Instead of letting Claude run commands that mutate your local Python packages, keep a managed, documented venv it can use across all sessions. See [[uv]].
`curl -LsSf https://astral.sh/uv/install.sh | sh`
`powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
Once those are done, you have everything you need to follow the rest of this note.

## Start Here

If you only do three things, do these:

1. Open [[HOME]] to see the vault dashboard.
2. Create a note at `04 Notes/`.
3. Install the web clipper extension and add a webpage to `01 Raw Sources/`.

## How This Vault Is Organized

The folder names are numbered on purpose. They represent a context refinement hierarchy and a structured reference to break up types of files.
![[Welcome-260415-30.png]]

### Basic vs Advanced layout

You will notice there is a `_05 Adv/` folder tucked at the bottom of the tree. That is the **advanced** layout, shown populated as an example. You can start in the **basic** layout and graduate when the basic layout stops fitting. Eventually create the Wiki from sources. No reason to pre-build and manage structure you don't have content for yet.

This vault attempts to scaffold out a ladder for these different levels of context refinement and information type. However, obsidian in general is not meant to be a one size fits all or be a structure you set on day one. Ultimately the vault should be a growing system and modified to the users needs. There is space at `06` and `09` for Classes, Certificates, Work, Career, Health, any other major knowledge sources worth a dedicated root numbered folder.

**Basic (start here).** One folder for your thinking (`04 Notes/`), one for navigation (`05 Menus/`). Subfolder inside `04 Notes/` by topic (`04 Notes/Programming/`, `04 Notes/Work/`, etc.). MOCs and indexes live in `05 Menus/`. This is enough until you have more notes.

**Advanced (migrate later).** The `04`-tier splits into three layers: `03 Wiki/` for distilled, stable source reference notes you return to; `04 Ideas/` for working drafts and project notes; `05 Crystal/` for synthesized Maps of Content and focus hubs. Peek inside `_05 Adv/` to see the shape. Realizing this resembles [[Zettelkasten]] and that should be adopted more.

**When to migrate.** When enough sources are being referenced and synthesized review Karpathy Wiki LLM research and try to develop an agent to manage these connections in `03 Wiki/`. When a cluster of notes starts to become outdated, duplicated, disorganized lift a reference and takeaways note linking relevant current Idea notes in `05 Crystal/`. `04 Ideas/` becomes your spot to dump your thinking and LLM collaboration into or you can leave it as `04 Notes/.

The commands (`/note`, `/moc`, `/crystal`) are written against whichever `04` folder you are using — they do not care if the folder is named `Notes` or `Ideas`. `/moc` is for basic table of contents, `/crystal` for a curated organized reference.

### Folder reference

Current basic layout plus the persistent top-level folders:

| Folder                 | Purpose                                                       |
| ---------------------- | ------------------------------------------------------------- |
| `Inbox/`               | Fast capture and temporary landing zone                       |
| `00 Attachments/`      | Pasted images and files, topic-organized                      |
| `01 Raw Sources/`      | PDFs, transcripts, copied source material                     |
| `02 Calendar/`         | Daily notes named `YYYY-MM-DD.md`                             |
| `04 Notes/`            | Your main thinking and project notes (basic default)          |
| `05 Menus/`            | Maps of Content and navigation notes                          |
| `06 Courses/`          | If you are a student create this directory                    |
| `06 Deliverables/`     | If you are using this for work create this directory          |
| `07 Workspaces/`       | Repeatable project/work session setups, [[MWP]]               |
| `08 Code/`             | Tooling and technical reference notes                         |
| `09 Spare/`            | Can use for tracking health, career, travel, other life stuff |
| `10 CLAUDE/`           | Claude Code project config (commands, skills, agents)         |
| `11 GEMINI/`           | Gemini CLI project config (ext mcp and email identity)        |
| `12 PI/`               | Pi coding agent directory (in progress custom harness)        |
| `13 Codex or Copilot/` | Codex/Copilot CLI harness config (available)                  |
| `Clippings/`           | Saved web articles and imported reads                         |
| `config/Templates/`    | Templates used when creating notes                            |
| `_05 Adv/`             | Advanced-layout sample content — reference or delete          |

## Good Places to Explore First

There is already useful material in this vault.

### In `_05 Adv/04 Ideas/Obsidian/`

- [[Obsidian Commands 1]]
- [[Obsidian Skills Starter Pack]]
- [[Vault Organization and Menu System]]
- [[How I'm Using Claude Code + Obsidian As a Non-Technical Person 1]]

These live in the advanced-layout sample and explain 
- the starter command-driven workflow and 
- how to build your own, note patterns, and 
- how other people are actually using a setup like this. 

An idea file may be of varying level of quality — don't necessarily read them end to end; use an LLM to query the information you want and break it down iteratively. Write your own note from them.

## Your First 10 Minutes

### 1. Open the dashboard

Start with [[HOME]]. It surfaces recent files and the main areas of the vault.

### 2. Open today's note

Daily notes live in `02 Calendar/`. They are the easiest place to capture to-do tasks, events, and loose thinking.

### 3. Create one note

Do it in obsidian ctrl+n or

Ask Claude Code:

```text
/note My First Note
```

That creates a note in `04 Notes/` using one of the vault templates. You likely won't use this all the time but a good habit to use templates as your starting point for notes. Good for future properties tags and consistent vault structure for organization and note merges.

### 4. Add one task to today's daily note

```text
/daily add todo Read the welcome note and explore HOME
```

### 5. Follow a few links

Open a note, click a few `[[wikilinks]]`, and get a feel for how ideas connect.

## Useful Claude Commands

You do not need to memorize these, but these are the most practical ones to start with:

| Command           | What it does                                                          |
| ----------------- | --------------------------------------------------------------------- |
| `/daily`          | Today's daily note hub — view, add to-dos, add events                 |
| `/current`        | Loads the note currently open in Obsidian                             |
| `/note Title`     | Creates a new note from an inferred template                          |
| `/moc folder`     | Builds a Map of Content (navigation note) for a folder or tag         |
| `/pickup`         | Summarizes recent vault activity                                      |
| `/focus MOC name` | Loads a topic and linked notes for deep work, save session on unfocus |
| `/sync`           | Pulls and rebases the latest vault changes from your git remote       |

Plain English works just as well. The clearer your request, the better the result — a well-phrased ask is a kind of skill in itself. Try things like:

- "Make a note about my onboarding ideas."
- "Create a Map of Content for `04` / `Obsidian`."
- "Find unfinished tasks related to setup."

## A Few Concepts Worth Knowing

### Wikilinks

`[[Note Name]]` links one note to another. This is the core mechanic of Obsidian.

### Properties

The YAML block at the top of a note stores metadata like `title`, `tags`, and dates.

### Templates

This vault already has templates in `config/Templates/`:

- `Chat`
- `Idea`
- `MOC`
- `py`
- `Service`
- daily note templates via `{{date}}.md`

Modify them to your liking, adapt them over time, or delete them.

### Maps of Content

`05 Menus/` holds navigation notes (Maps of Content) that help you browse a topic or folder without memorizing where everything lives. In the advanced layout, `05 Crystal/` also holds Crystal notes that synthesize ideas into structured refined working hubs.

## Suggested Next Steps

- [ ] Open [[HOME]]
- [ ] Read [[Obsidian Commands 1]] or [[Obsidian Skills Starter Pack]]
- [ ] Read one article from [[Build Your Second Brain With Claude Code & Obsidian]]
- [ ] Create a note with `/note`
- [ ] Add a task to today's daily note with `/daily`
- [ ] Run a real task — read a PDF and set up a uv claude Python venv

> [!quote]
> The value of this vault isn't in perfect organization or understanding on day one — it comes from adding notes, linking ideas, and distilling what works into skills and structure over time. The scaffolding compounds.

When this note has done its job, archive it. [[HOME]] is the place you'll return to most.
