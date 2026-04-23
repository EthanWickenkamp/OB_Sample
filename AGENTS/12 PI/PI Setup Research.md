---
tags:
  - pi-agent
  - research
  - setup
status: researched
---

# PI Setup Research

Scaffolded the `12 PI/` directory with stub agents (chat, vault-tools, youtube-summary) and a top-level `PI.md` config modeled after the CLAUDE.md/GEMINI.md pattern. The structure is ready but the following needs to be verified against the actual pi-coding-agent before this is production-ready.

## What's in place

- `PI.md` — top-level config (mirrors CLAUDE.md pattern)
- `12 PI/agents/chat/agents.md` — general chat agent
- `12 PI/agents/vault-tools/agents.md` — link finder, orphan finder, tag audit
- `12 PI/agents/youtube-summary/agents.md` — structured YouTube summaries
- Vault boundary pattern from the video (agents can only write to their own directory by default)

## Research needed

### 1. AGENTS.md loading behavior
- Does Pi read `AGENTS.md` (uppercase) or `agents.md` (lowercase)? The video showed lowercase but the repo note references uppercase.
- Is it read from cwd only, or does Pi walk up the directory tree like Claude reads `CLAUDE.md`?
- Does it support frontmatter for routing (`description`, `use when`) or is it pure prose?

### 2. `.pi/` directory convention
- What goes in `.pi/prompts/`? Filename-driven routing or something else?
- What goes in `.pi/extensions/`? The repo has ~80 example extensions — which ones are relevant for an Obsidian vault setup?
- Is there a `.pi/settings.json` equivalent? What config options exist?
- Does `~/.pi/` serve as a global config (like `~/.claude/`)?

### 3. Session persistence
- Sessions persist as JSONL under `~/.pi/agent/sessions/` per the repo note
- The session tree uses id/parentId for branching — is this automatic or opt-in?
- Can session history be redirected to a vault-local path (e.g., `12 PI/sessions/`)?

### 4. Extension system priorities
From the ~80 example extensions in `packages/coding-agent/examples/extensions/`, which ones matter for vault work:
- `protected-paths` — enforce the vault boundary restriction
- `dirty-repo-guard` — prevent working on uncommitted changes
- `git-checkpoint` — auto-commit before risky operations
- `permission-gate` — user confirmation for writes outside agent dir
- `plan-mode` — planning before execution
- Any others relevant to Obsidian note management?

### 5. Provider configuration
- How does Pi select the model provider? CLI flag, env var, config file?
- Can it be pointed at local models (Ollama, vLLM) for lightweight tasks like the video showed (using Gemini for YouTube summaries instead of Opus)?
- What's the model switching story per-agent (different model for different agent folders)?

### 6. Tool registration
- Pi has built-in tools (read/write/edit/bash/grep/find/ls). Can custom tools be added?
- Could the Obsidian CLI commands be registered as Pi tools for tighter integration?
- Does Pi support MCP servers the way Claude Code does?

### 7. Integration with Claude Code
- Per the vault's design philosophy, Claude Code is the engine and other agents are sub-engines wired in behind it.
- Pi's RPC mode (JSONL over stdio) is the candidate integration point — can Claude Code spawn Pi as a subprocess for specific jobs?
- What would the Claude Code skill look like that delegates to a Pi agent?

## What I'd change immediately if I had answers

1. **AGENTS.md casing** — rename if Pi expects uppercase
2. **Protected paths extension** — enable it and configure vault boundary as a proper extension rather than relying on prose instructions in agents.md
3. **Provider config** — set a default model and allow per-agent overrides (Opus for complex work, Gemini/Sonnet for summaries)
4. **Session redirect** — point session storage into `12 PI/sessions/` so history is visible in the vault
5. **Add Python scripts** — the video showed Python scripts alongside agents (transcript fetcher, vault scanner). These should be in the agent folders.

## Answers

*Verified against `~/OpenSource/pi-mono/packages/coding-agent/src/` — 2026-04-12*

### 1. AGENTS.md loading behavior

- **Uppercase.** `resource-loader.ts:58` checks `AGENTS.md` first, falls back to `CLAUDE.md`: `const candidates = ["AGENTS.md", "CLAUDE.md"];`
- **Walks up the directory tree** from cwd to root, collecting all matches (`resource-loader.ts:92-107`). Also loads global context from `~/.pi/agent/` first. This mirrors Claude Code's `CLAUDE.md` tree-walk behavior.
- **Frontmatter supported.** Uses `parseFrontmatter()` from `utils/frontmatter.ts` — standard YAML between `---` delimiters.
- **Action:** Rename `agents.md` → `AGENTS.md` in all three stub agent directories.

### 2. `.pi/` directory convention

**Global `~/.pi/agent/` structure:**

| Path | Purpose |
|------|---------|
| `settings.json` | User settings (settings-manager.ts:215) |
| `models.json` | Custom model definitions (line 205) |
| `auth.json` | API keys and OAuth tokens (line 210) |
| `prompts/` | Global prompt templates (line 230) |
| `skills/` | Global skills (skills.ts:452) |
| `themes/` | Custom themes (line 200) |
| `tools/` | Custom tools (line 220) |
| `bin/` | Managed binaries — fd, rg (line 225) |
| `sessions/` | Session storage (line 235) |

**Project `.pi/` structure (at project root, not inside `12 PI/`):**

| Path | Purpose |
|------|---------|
| `settings.json` | Project-local settings, merged over global (settings-manager.ts:148) |
| `prompts/` | Project-local prompt templates (resource-loader.ts:252) |
| `skills/` | Project-local skills (skills.ts:453) |
| `extensions/` | Project-local extensions |

**Precedence:** Project `.pi/settings.json` overrides global `~/.pi/agent/settings.json`, merged recursively.

**Key insight:** `.pi/` goes at the project root (vault root for us), not inside `12 PI/`. The OB_Sample scaffolding had this wrong.

### 3. Session persistence

- **Default path:** `~/.pi/agent/sessions/<encoded-cwd>/<timestamp>_<sessionId>.jsonl` (session-manager.ts:423-429)
- **Path encoding:** cwd with `/\:` replaced by `-`, e.g. `--home-fish-OB-OB_Claude--`
- **Redirectable:** Yes, three ways:
  1. CLI flag: `--session-dir <path>` (main.ts:456) — highest priority
  2. Settings: `sessionDir` field in `settings.json` (settings-manager.ts:97)
  3. Extension hook: `session_directory` event handler (main.ts:402-412)
- **Format:** JSONL, session version 3. Header with id/timestamp/cwd, then entries: messages, model changes, thinking levels, compactions, branches.
- **Branching:** Session tree uses `parentId` pointer moves, not file copies (session-manager.ts:833-910). `/tree` walks the graph.
- **Verdict:** Keep default storage. Redirecting into `12 PI/sessions/` is possible but would pollute the vault with JSONL files that aren't markdown notes. If we want visibility, write a skill that summarizes sessions into markdown.

### 4. Extension system priorities

Extensions load via `jiti` (dynamic TS import) from `.pi/extensions/` or `~/.pi/agent/extensions/`. The full hook surface is in `extensions/types.ts`:

**Lifecycle hooks:** `session_start`, `session_switch`, `session_fork`, `session_compact`, `session_shutdown`, `before_agent_start`, `agent_start`, `agent_end`, `turn_start`, `turn_end`

**Message hooks:** `message_start`, `message_update`, `message_end`

**Tool hooks:** `tool_execution_start`, `tool_execution_update`, `tool_execution_end`, `tool_call` (with per-tool variants: bash, read, edit, write, grep, find, ls, custom)

**Registration API:** `registerTool()`, `registerCommand()`, `registerShortcut()`, `registerFlag()`, `registerMessageRenderer()`, `registerProvider()`

**Relevant extensions from the ~80 examples:**

| Extension | Why it matters | Priority |
|-----------|---------------|----------|
| `protected-paths` | Enforce vault boundary (only write to `12 PI/`) as code, not prose | High |
| `permission-gate` | User confirmation for writes outside agent dir | High |
| `plan-mode` | Think before executing — useful for vault reorganization tasks | Medium |
| `git-checkpoint` | Auto-commit before risky operations — vault is git-backed | Medium |
| `dirty-repo-guard` | Prevent working on uncommitted changes | Low (vault auto-commits) |

### 5. Provider configuration

**Selection priority (main.ts:509-570):**
1. **CLI flags** (highest): `--provider <name> --model <pattern>` or `--model <provider>/<pattern>` or `--model <pattern>:<thinking>`
2. **Settings:** `defaultProvider` and `defaultModel` in `settings.json`
3. **Fallback:** First available scoped model

**API keys:** CLI `--api-key`, env vars (checked by providers), or `~/.pi/agent/auth.json`

**Local model support:** Pi has a provider registration system (`registerProvider()`). The built-in providers are OpenAI, Anthropic, Google, Bedrock, Mistral, Vertex. Ollama/vLLM would need a custom extension or the OpenAI-compatible endpoint trick.

**Per-agent model switching:** Not native per-directory. You'd set the model via CLI flag when launching from a specific agent directory, or use an extension on `model_select` to route based on cwd.

**Our plan:** Use Gemini or a cheap Anthropic model (Haiku) as the default. Pi is the token-saver — don't run Opus through it.

### 6. Tool registration

- Built-in tools: `read`, `write`, `edit`, `bash`, `grep`, `find`, `ls` (in `src/core/tools/`)
- Custom tools: Yes, via `registerTool()` in extensions
- Obsidian CLI: Can be called through `bash` tool. For tighter integration, wrap the CLI commands as registered tools via an extension.
- **No MCP support.** Grep for "mcp"/"MCP" in the codebase returns nothing relevant. qmd cannot be wired in as an MCP server — it would need to go through bash (`qmd search "..."`) or a custom tool extension that shells out to qmd.

### 7. Integration with Claude Code

- **RPC mode** is the integration point. Pi runs as `pi --mode rpc` and accepts JSONL commands on stdin, emits JSONL events on stdout (`modes/rpc/rpc-mode.ts`).
- **Command vocabulary:** `prompt`, `steer`, `follow_up`, `abort`, `set_model`, `cycle_model`, `compact`, `get_session_stats`, `switch_session`, `fork`, `new_session`, `export_html`
- **Claude Code skill design:** A `/pi` skill that spawns `pi --mode rpc --session-dir <path>` as a subprocess, pipes a prompt, collects the response, and returns it. Similar to how Codex and Gemini are already wired in.
- **Not a sub-engine in the Codex sense.** Pi is a full competing harness. The RPC mode makes it callable, but it runs its own agent loop, tool execution, and compaction. Think of it as "ask lil bro to handle this" rather than "delegate a subtask to a worker."

## Source material

- [[YouTube - hhtExS5UQBI]] — Obsidian + Pi demo video
- [[pi-mono]] — repo analysis in `03 Code/OpenSource AI/Repos/`
- Pi repo: `badlogic/pi-mono` on GitHub
- Extension examples: `packages/coding-agent/examples/extensions/`
