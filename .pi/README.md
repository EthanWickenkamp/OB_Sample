# .pi/ — Pi project config

Project-local config for the [pi coding agent](https://github.com/badlogic/pi-mono) (`@earendil-works/pi-coding-agent`). Merged over the global `~/.pi/agent/settings.json` at launch. Human-facing docs live in the vault at `AGENTS/12 PI/PI.md`.

Verified against pi **v0.81.1**.

| File | Purpose |
|------|---------|
| `settings.json` | Default provider/model. Pi is the token-saver — default is Haiku; override per-launch with `--model <provider>/<pattern>`. |
| `extensions/protected-paths.ts` | Write boundary: silent writes only inside `AGENTS/12 PI/` and `Inbox/`; confirmation dialog elsewhere; `.git/`, `.obsidian/`, `.pi/`, `10 CLAUDE/` always blocked. Bash is NOT gated — see the file header. |
| `prompts/orient.md` | Sample prompt template. Filename = slash command (`/orient`); same frontmatter pattern as Claude Code commands. Add your own alongside it. |

Auth: `pi` prompts for provider login on first run (stored in `~/.pi/agent/auth.json`), or set `ANTHROPIC_API_KEY` in the environment.

Note: Pi reads `AGENTS.md` walking up from its launch directory. Launching from an agent folder (`AGENTS/12 PI/agents/<name>/`) picks up `AGENTS/AGENTS.md` on the walk; launching from the vault root requires an `AGENTS.md` at the root.
