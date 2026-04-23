## Claude Code — Anthropic's CLI Agent

Claude Code is Anthropic's official command-line tool for Claude. You run it inside a folder (like this vault), and it can read, write, and edit files, run commands, and answer questions with the folder as its context.

### What it is

- A **terminal app** — you start it in a directory and it works with the files in that directory
- An **agent** — it can take multi-step actions (read files, edit them, run commands) rather than just answering one question at a time
- **Shell Access** — your files stay on your machine; Claude only sees what it reads during the session

In this vault, Claude Code is the thing that runs [[inbox/Obsidian Commands]] like `obsidian outline`, `/today`, `/note`, and `/menu`.

---

### Prerequisites

Before you install Claude Code, you need:

1. A **terminal** — [[Git Bash]] on Windows, Terminal on Mac, any shell on Linux
2. **Node.js** (version 18 or newer) — install through [[nvm]] so you can upgrade cleanly
3. An **Anthropic account** — sign up at [claude.ai](https://claude.ai) or [console.anthropic.com](https://console.anthropic.com)

---

### Install

Once Node is installed, Claude Code is a single npm command:

```bash
npm install -g @anthropic-ai/claude-code
```

Verify it's installed:

```bash
claude --version
```

> [!note] Permission errors on install?
> If `npm install -g` complains about permissions, it means Node was installed system-wide instead of through nvm. Reinstall Node via [[nvm]] — nvm puts everything in your home folder, so global installs don't need admin rights. <--- is this actually true?

---

### First run

1. Open your terminal and `cd` into the folder you want Claude to work in. For this vault:

   ```bash
   cd ~/OB/OB_Sample
   ```

2. Start Claude Code:

   ```bash
   claude
   ```

3. The first time you run it, Claude will walk you through authentication in your browser. You can sign in with either: Or use [[Ollama]] to run it locally, >12gb vram
   - A **Claude Pro / Max subscription** (claude.ai account)
   - An **Anthropic API key** (from console.anthropic.com, pay-as-you-go)

4. Once authenticated, you're in an interactive session. Type a request in plain English or use a slash command like `/today`.

To end a session, type `/exit` or press Ctrl+C twice.

---

### Basic usage

```text
# Ask a question about the vault
What notes do I have about Obsidian?

# Ask Claude to do something
Create a note called "Weekend Trip Ideas" in 04 Notes/.

# Use a slash command
/today
/note My New Note
```

Plain English and slash commands both work — slash commands are just shortcuts for common tasks. See [[inbox/Obsidian Commands]] for the full list.

---

### The mental model

```
You            →  type a request
Claude Code    →  reads files, edits files, runs commands
Your vault     →  the only context it sees
```

- Claude only reads files it decides are relevant to your request
- Every edit it makes happens on your local disk — nothing uploads except the text Claude reads or writes
- You can always stop it mid-action with Ctrl+C

---

### Switching accounts or re-authenticating

```bash
# Inside a Claude Code session
/login
```

That opens the browser auth flow again so you can switch between subscription and API key, or sign into a different account.

---

### See also

- [[Git Bash]] — the terminal you run Claude Code from on Windows
- [[nvm]] — how to install Node, the prerequisite for Claude Code
- [[inbox/Obsidian Commands]] — the slash commands this vault already has set up

> [!tip] Where to learn more
> The official docs live at [claude.com/claude-code](https://claude.com/claude-code). `/help` inside a session also shows the built-in commands.
