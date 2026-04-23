---
name: to-sample
description: Generalize a reference file or command from your vault into a template-worthy version for OB_Sample — strips personal state, rewrites paths, softens tone for less technical users, and stubs out customization points.
argument-hint: source path in your vault (e.g. `08 Code/Python/uv.md` or `.claude/commands/focus.md`)
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Take a file from your own vault and prepare a template-worthy version for **OB_Sample** — the shared template this vault is based on. `$ARGUMENTS` is the source path.

Generalizing a file you use well and sending it back to OB_Sample is how the template stays alive. Every file you clean up and contribute saves the next person a half-hour of figuring out your workflow from scratch.

---

## What makes something template-worthy

The test to apply on every pass:

- **No personal state** — no real paths, bearer tokens, hostnames, device audit tables, version pins, or class/project names from your vault
- **Stubs, not secrets** — anything the next person must fill in becomes a clearly marked placeholder, not a blank or a leftover real value
- **Hooks, not dumps** — if content depends on external setup (auth, Python env, git remote), replace the heavy block with a one-liner and a link to a setup note in `config/`
- **Analogy over jargon** — less technical users are the audience. Where a line reads like a man page, swap in a short analogy or a "why this exists" sentence
- **Philosophy where it fits** — a sentence or two on *why the vault is organized this way* earns its keep when it helps a new user feel oriented
- **Structure matches OB_Sample** — folders, file counts, and cross-references use the sample's layout, not yours

Think of it this way: the file has to stand on its own when a stranger opens it cold, without any of the context you carry. If your future self — opening it on a fresh device with none of today's mental state — could still follow it, it's template-worthy.

---

## Step 1: Read the source

Read `$ARGUMENTS`. If it's a command in `.claude/commands/`, also read any sibling skills it references.

Read these for target-side context:

- `OB_Sample/10 CLAUDE/CLAUDE.md` — the sample vault's canonical tone and folder list
- `OB_Sample/` top level (via `ls`) — actual folder numbers and names today

Note your own vault's layout from `10 CLAUDE/CLAUDE.md` so you know what maps to what.

---

## Step 2: Pick the target path

Every vault organizes folders differently — your `04 Ideas/` might be someone else's `04 Notes/`. You'll need to build a mapping from **your vault's structure** to **OB_Sample's structure**.

Start by listing both:

```bash
ls OB_Sample/                    # target structure (the canonical layout)
ls .                             # your vault root
```

Then build a mapping for your own vault. This is an example — replace the left column with your actual folders:

| Your vault | → | OB_Sample |
|---|---|---|
| `<your code folder>` | → | `08 Code/` |
| `<your ideas / notes folder>` | → | `04 Notes/` |
| `<your MOC / index folder>` | → | `05 Menus/` |
| `<your classes folder>/<school>/<class>/` | → | `09 Classes/<placeholder>/` |
| `<your daily notes folder>` | → | `02 Calendar/` |
| `.claude/commands/<n>.md` | → | `OB_Sample/10 CLAUDE/commands/<n>.md` |
| `.claude/skills/<n>/` | → | `OB_Sample/10 CLAUDE/skills/<n>/` |

If the file doesn't map cleanly, stop and ask the user where it should live.

If OB_Sample has no equivalent folder for what you're contributing — for example, deeply personal notes (health, career, homelab configs) — that file may not belong in the template at all. Ask before proceeding.

---

## Step 3: Mechanical pass (no judgment needed)

Apply these without asking:

1. **Strip bearer tokens** — any `Authorization: Bearer <token>` disappears. If a CLI equivalent exists (`obsidian file`, `obsidian daily:read`, etc.), replace the whole REST block with the CLI call
2. **Rewrite hardcoded paths** — apply your Step 2 mapping to every path reference inside the file
3. **Drop device tables** — "Per-device audit status", "Last audited", hostname rows all go
4. **Strip version pins** — remove version numbers from library tables and inline mentions; describe libraries by purpose instead
5. **Remove real names** — class codes (e.g. `CS 101`, `MATH 200`), school names, hostnames (e.g. `home-pc`, `laptop-work`), personal project names, real people — replaced with generic placeholders or removed

---

## Step 4: Judgment pass (ask per item)

For each of these, surface it and ask before editing. Don't guess:

- **Personal references that might still work as examples** — show each one, ask `[keep / stub / drop]`
- **Large inlined setup blocks** — sections that mostly document how *your* environment is set up. Offer to replace with a one-liner pointing to a setup note (`config/setup-python.md`, etc.)
- **Ambiguous folder mappings** — anything Step 2 flagged as "ask"
- **Sections that might not belong in a template at all** — personal audit logs, private notes, ephemeral state

Present as a numbered list so the user can answer in one pass:

```
Judgment calls on <filename>:
1. <thing> — [keep / stub / drop]
2. <thing> — [keep / stub / drop]
...
```

---

## Step 5: Tone pass (less technical users)

The person reading the generalized version may not be the power user you are — they might be a curious note-taker who installed Obsidian and Claude Code last weekend. Write for them:

- **Swap jargon for analogies** where the analogy actually helps. Don't force analogies where the technical term is clear — "venv" is fine, dense implementation detail is not. Think: "uv is like a single toolbox that used to be three — a package installer, an environment maker, and a Python version manager, all in one"
- **Add a 1–2 sentence "why this exists" framing** at the top of technical sections. What problem does it solve? What does it unlock for their notes?
- **Warm the voice slightly** — "Run this" → "You'll run this once"; "Do X" → "This is where you'll X". Don't overdo it; just enough that the file reads like a guide, not a man page
- **Sprinkle philosophical vault framing sparingly** — one or two sentences where it helps a new user see how this file fits the rest of the system. Not every file needs it. Think "why one venv, not many" or "why `02 Calendar/` holds your daily notes" — short, concrete, grounded. Never preach

---

## Step 6: Stub and hook pass

- **Stubs the user must fill in** — marked clearly: `<your-vault-name>`, `<your class structure here — fill out each term>`, `<TODO: ...>`. One clear stub beats three vague ones
- **Hooks to setup guides** — "See `config/setup-python.md` for the initial install". If the setup note doesn't exist yet, list it so the next contributor can create it later. Track every hook added so you can report them at the end
- **Front matter** — for command files, preserve the original `name`, `description`, `allowed-tools`; re-generalize any argument hint

---

## Step 7: Show the diff and confirm

Before writing, show the user:

1. **Target path** — where it will land in OB_Sample
2. **Summary of changes** — bullet list grouped by pass (mechanical / judgment / tone / stub)
3. **New hooks added** — any `config/` setup notes to create later
4. **Preview** — full generalized file if short (<100 lines), or a diff against the source if long

Ask: *"Write to `<target path>`? [y / edit / cancel]"*

- **y** — write the file, confirm the path, remind the user of any hook notes
- **edit** — let the user point to specific lines to revise, then re-show
- **cancel** — stop, write nothing

---

## Step 8: Write and report

On approval:

- Write the file to its target path
- Print: `Generalized → OB_Sample/<path>`
- List any setup-note hooks to create later
- If the source was a `.claude/commands/` file, remind the user to check that `OB_Sample/10 CLAUDE/CLAUDE.md` references it correctly

---

## Notes

- Run this **one file at a time** — the judgment pass is per-file, don't batch
- If the source is already in OB_Sample or outside your vault, stop and flag it
- Never write to `OB_Sample/` without Step 7 confirmation — it's a shared template, every change should be intentional
