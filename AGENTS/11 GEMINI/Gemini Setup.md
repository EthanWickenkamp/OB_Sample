## Gemini CLI — Setup

For the rationale behind this integration see [[Gemini Rationale]].

### Install

Gemini CLI runs on Node, so [[nvm]] + Node need to be set up first (same as [[Claude Code]]).

```bash
npm install -g @google/gemini-cli
```

Verify:

```bash
gemini --version
```

The first time you run `gemini` it walks you through auth — sign in with a Google account or provide a Gemini API key from [aistudio.google.com](https://aistudio.google.com).

---

### MCP Servers

Configure MCP servers in `~/.gemini/settings.json` under `mcpServers` — the shape is nearly identical to Claude Code's MCP config, so entries can usually be copy-pasted between the two. This keeps Claude's context window completely free of MCPs.

```json
{
  "mcpServers": {
    "serverName": {
      "command": "path/to/server",
      "args": ["--arg1", "value1"],
      "env": { "KEY": "value" }
    }
  }
}
```

Once connected, all MCP tools are available during `gemini --yolo -p "…"` calls. See [[MCP servers with Gemini CLI]] for full configuration reference.

---

### Extensions

Extensions are not in a great state right now but are expected to improve.

- [Browse Extensions](https://geminicli.com/extensions/)
- [Extensions docs](https://geminicli.com/docs/extensions/)
- [Best practices](https://geminicli.com/docs/extensions/best-practices/)

```bash
gemini extensions list
gemini extensions install <source>
gemini extensions enable <name>
```
