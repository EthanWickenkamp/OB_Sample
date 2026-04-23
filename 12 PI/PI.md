# PI.md

Pi agents can do specialized vault management tasks. Further research necessary for integration — what's here is exploratory, not settled configuration.

Reference note for the Pi coding agent setup in this vault. Pi reads `AGENTS.md` (not this file) as its system prompt — this is a human-facing reference.

## How Pi Works in This Vault

Pi reads `AGENTS.md` at the vault root as global context, then walks up from cwd collecting any additional `AGENTS.md` files. Agent-specific folders in `12 PI/agents/` each have their own `AGENTS.md` that adds specialized instructions.

**Launch patterns:**
```bash
# General vault work (reads vault-root AGENTS.md)
cd ~/OB/OB_name && pi

# Specific agent (reads agent AGENTS.md + vault-root AGENTS.md)
cd ~/OB/OB_name/12\ PI/agents/chat && pi

# With model override
cd ~/OB/OB_name/12\ PI/agents/youtube-summary && pi --model google/gemini-2.5-flash
```

## Directory Layout

```
OB_name/                          ← vault root
├── AGENTS.md                     ← Pi reads this (global context)
├── .pi/                          ← Pi project config (at vault root, not inside 12 PI/)
│   ├── settings.json             ← provider, model defaults
│   ├── prompts/                  ← shared prompt templates
│   ├── skills/                   ← shared skills
│   └── extensions/               ← TypeScript extensions
│       └── protected-paths.ts    ← vault boundary enforcement
├── 12 PI/                        ← Pi workspace (visible in Obsidian)
│   ├── PI Setup Research.md      ← research and config reference
│   └── agents/                   ← per-agent directories
│       ├── chat/AGENTS.md
│       ├── vault-tools/AGENTS.md
│       └── youtube-summary/AGENTS.md
```

**Key distinction:** `.pi/` lives at vault root (Pi convention). `12 PI/` is the visible workspace in Obsidian where agents write their output.

## Configuration

**Settings:** `.pi/settings.json` — project-local, merges over global `~/.pi/agent/settings.json`.

**Default provider:** Google (Gemini 2.5 Flash). Pi is the token-saver — don't run Opus through it. Override per-launch with `--model`.

**Extensions:** `.pi/extensions/` — loaded automatically via jiti. Currently:
- `protected-paths.ts` — enforces write boundary to `12 PI/` only, prompts for confirmation on writes elsewhere.

**Sessions:** Stored at `~/.pi/agent/sessions/` (default). Not redirected into vault — JSONL files aren't markdown notes.

## Agents

| Agent | Directory | Purpose | Suggested model |
|-------|-----------|---------|-----------------|
| Chat | `12 PI/agents/chat/` | General vault Q&A, exploration | Default (Flash) |
| Vault Tools | `12 PI/agents/vault-tools/` | Link finder, orphans, tag audit | Default (Flash) |
| YouTube Summary | `12 PI/agents/youtube-summary/` | Structured video summaries | Default (Flash) |

## What Pi Has vs Claude Code

| Feature | Pi | Claude Code |
|---------|-----|-------------|
| System prompt | ~200 tokens | ~10,000 tokens |
| Built-in tools | 7 (read, write, edit, bash, grep, find, ls) | ~40 |
| Safety mode | YOLO (none) | Permission gates |
| Extensions | ~80 examples, hot-swappable TS | Hooks + settings |
| MCP support | No | Yes |
| Memory system | None (file-system only) | Auto-memory + project memory |
| Provider lock-in | None (15+ providers) | Anthropic only |
| Self-modification | Full (reads/edits own code) | No |

## No MCP

Pi does not support MCP servers. Obsidian CLI and other tools go through the bash tool. For tighter integration, wrap CLI commands as registered tools via a custom extension in `.pi/extensions/`.

## Integration with Claude Code

Pi can be called from Claude Code via RPC mode:
```bash
pi --mode rpc --session-dir <path>
```
Commands over stdin (JSONL): `prompt`, `steer`, `follow_up`, `abort`, `set_model`, `compact`, etc. A `/pi` Claude Code skill could spawn Pi as a subprocess for lightweight jobs.

## Related

- [[AGENTS]] — the file Pi actually reads
- [[PI Setup Research]] — full research with source verification
- [[OBPI]] — project note in the parent vault's OpenSource AI folder
