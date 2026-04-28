---
tags:
  - workspace
  - banana
  - image-generation
type: setup
status: draft
created: 2026-04-12
---

# NanoBanana Workspace Setup

Multi-engine image generation workspace. Claude crafts the prompt using the 5-component banana skill, kicks to Gemini CLI for execution via the `/nano-banana` extension. The Gemini CLI is sort of unnecessary at the moment but I assume a day will come there is an optimal fully native plugin extension for Gemini CLI.

## Pipeline

```
Claude Code                    Gemini CLI                      Vault
───────────                    ──────────                      ─────
/banana generate <idea>  →  gemini --yolo -p "/nano-banana  →  renders/
                               <crafted prompt>"                 (embedded)
```

1. **Claude** — Creative Director. Reads the project's layout + style notes. Constructs the full 5-component prompt (Subject → Action → Location/Context → Composition → Style). Never passes raw user text.
2. **Gemini** — Executor. `gemini --yolo -p "/nano-banana <prompt>"` runs the nano-banana extension with no confirmation gates. Gemini handles the API call and image generation.
3. **Vault** — Results land in the project's `renders/` note with embedded images. Not a folder of loose files — the renders note is the gallery.

## Project Structure

Each project is a folder under `07 Workspaces/NanoBanana/projects/`:

```
07 Workspaces/NanoBanana/
├── NanoBanana Setup.md          ← this file
├── CLAUDE.md                    ← project-level Claude instructions
└── projects/
    └── <project-name>/
        ├── layout.md            ← what the image contains: subjects, positions, composition, spatial relationships
        ├── style.md             ← visual style: the "image five" (camera, lighting, color, mood, reference), brand presets
        └── renders.md           ← generated results embedded inline, not dumped in a folder
```

### layout.md

Describes *what* is in the image and *where*. This is the Subject + Action + Location/Context + Composition components of the 5-component formula.

- Subjects and their positions (foreground, midground, background)
- Spatial relationships ("product centered, figure to the left")
- Composition rules (rule of thirds, symmetry, leading lines)
- Required elements ("MUST contain exactly three figures")
- Text placement if any (keep under 25 characters)

### style.md

Describes *how* the image looks. This is the Style component plus camera/lighting specifics.

- Camera and lens ("Sony A7R IV, 85mm f/1.4")
- Lighting setup ("golden hour rim light, soft fill from left")
- Color palette and mood
- Art direction references ("Vanity Fair editorial", "Bon Appetit feature spread")
- Domain mode (Cinema, Product, Portrait, Editorial, etc.)
- Aspect ratio and resolution defaults
- Brand preset name if applicable

### renders.md

The gallery. Each generation gets an entry:

```markdown
### <brief description>
![[<filename>.png]]
**Prompt:** <the crafted prompt that was sent>
**Model:** <model used> | **Ratio:** <aspect ratio> | **Date:** <timestamp>
```

Results embed directly. No separate attachments folder per project — images go to `00 Attachments/NanoBanana/` and get embedded here via wikilinks.

## CLAUDE.md (project-level)

```markdown
# NanoBanana Workspace

When working in this workspace, you are a Creative Director for AI image generation.

## Workflow

1. Read the project's `layout.md` and `style.md` before constructing any prompt
2. Use the banana skill's 5-component formula (Subject → Action → Location/Context → Composition → Style)
3. Construct the full prompt from layout + style notes
4. Execute via Gemini CLI: `gemini --yolo -p "/nano-banana <prompt>"`
5. Embed the result in the project's `renders.md`

## References

Full banana skill at `10 CLAUDE/skills/banana/SKILL.md`. Read `references/prompt-engineering.md` and `references/gemini-models.md` before every generation.
```

## Gemini Side

The `/nano-banana` extension must be installed in Gemini CLI. Reference: `11 GEMINI/Gemini CLI cheatsheet.md` and `11 GEMINI/MCP servers with Gemini CLI.md`.

`--yolo` flag = no confirmation prompts. Gemini executes the generation and returns the image path.

## TODO (needs polish)

- [ ] Write the actual `CLAUDE.md` file (currently in this setup note as a draft)
- [ ] Create a sample project with layout/style/renders stubs
- [ ] Verify `/nano-banana` extension install path and invocation syntax in Gemini CLI
- [ ] Decide: does Claude call `gemini --yolo` via bash, or does the user switch manually?
- [ ] Image output path convention — `00 Attachments/NanoBanana/<project>/` or flat?
- [ ] Cost tracking integration — does the banana skill's `cost_tracker.py` work across the Gemini CLI path?
- [ ] Preset system — can style.md reference banana presets from `~/.banana/presets/`?

## Related

- `10 CLAUDE/skills/banana/SKILL.md` — the full banana Creative Director skill
- `11 GEMINI/` — Gemini CLI configuration
- `references/prompt-engineering.md` — 5-component formula, domain modes, templates
