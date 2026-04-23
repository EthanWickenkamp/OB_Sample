## Gemini CLI — External Service & Extension

Gemini CLI is Google's terminal agent for the Gemini models. In this vault, we use it as an **external service** that [[Claude Code]] can call out to — think of it as an agent that Claude hands things off to when we want a task from Google services or other supported MCP. This keeps Claude's context window free and gives it full Gemini capabilities through the `gemini` command in the terminal, just like you would use it yourself. This is also great for image generation — Google's nano-banana is the best image model currently.

### What it is

- A **terminal agent**, similar in shape to Claude Code — you run `gemini` in a folder and it can read/edit files and run tools
- A **one-shot prompt mode** (`-p`) that takes a prompt, answers once, and exits — this is what makes it easy to call from inside Claude Code
- An **MCP client** — you can connect the same MCP servers you could use with Claude Code, so you have access to the same tools outside of Claude's context window.

---

### Why we use it here

| Claude Code alone | Claude Code + Gemini |
|---|---|
| One model, one perspective | Second opinion / alternate model on demand |
| Claude's context window for every task | Offload long-context work to Gemini |
| All token cost on Claude | Route cheap bulk tasks to Gemini |

This is a **minor integration** — Gemini is not the main driver. Claude Code stays in charge; it calls `gemini` the way it would call any other CLI tool. We also expect Gemini's external connections to improve going forward and potentially become the best option for that layer. Regardless, Claude is our main worker and doesn't need to worry about external services, only internal and the vault. 

---

For install, MCP, and extensions setup see [[Gemini Setup]].

---

### Calling Gemini from Claude Code

The pattern we use is a one-shot, auto-approved invocation:

```bash
gemini --yolo -p "/command description"
```

What each piece does:

- **`--yolo`** — auto-approves any tool actions Gemini wants to take, so the call doesn't hang waiting for a confirmation prompt. Required for non-interactive use.
- **`-p "…"`** — prompt mode. Takes the string, runs once, prints the answer, exits.
- **`/command description`** — a slash command registered in Gemini CLI (see `11 GEMINI/`), followed by whatever argument that command expects.

Because this is a single shell command, Claude Code can call it just like it calls `git` or `ls` — the result comes back as stdout and Claude reads it.

> [!tip] Why `--yolo` here
> Without it, Gemini pauses for `Approve? (y/n)` any time it wants to use a tool. That's fine interactively, but it deadlocks a non-interactive call from Claude Code. `--yolo` is the "this is a tool call with scripted context, just do it" switch.

---

### Gemini Extensions and MCPs

We connect the same MCP servers to Gemini that we use with Claude Code. Configure them in `~/.gemini/settings.json` under `mcpServers` — the shape is nearly identical to Claude Code's MCP config, so you can usually copy-paste entries between them. This keeps Claude's context window completely free of MCPs.

Once connected, any MCP tool is available to Gemini during a `gemini --yolo -p "…"` call.

References:
[Browse Extensions | Gemini CLI](https://geminicli.com/extensions/)
[Gemini CLI extensions | Gemini CLI](https://geminicli.com/docs/extensions/)
[Gemini CLI extension best practices | Gemini CLI](https://geminicli.com/docs/extensions/best-practices/)

Honestly, Gemini CLI extensions are not in a great state right now but I expect them to improve greatly.

---

### Mental model

```
You  →  Claude Code  →  shell: `gemini --yolo -p "/command …"`  →  Gemini  →  reply
              ↑                                                        ↓
              └─────────────────── answer comes back ←───────────────────┘
```

1. Output as stdout directly into Claude's context
2. Gemini modifies, adds, or executes something in the vault directly, maybe stdout "done" to Claude

---

### See also

- [[Claude Code]] — the primary driver; Gemini is called from here
- [[nvm]] — Node is the prerequisite
- [Gemini CLI docs](https://geminicli.com/docs/)
