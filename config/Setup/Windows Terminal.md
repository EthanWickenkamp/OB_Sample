# Windows Terminal

A custom **Windows Terminal** profile that opens a Git Bash shell directly into your vault and launches Claude Code on startup. One click and you are sitting at a Claude prompt inside the vault — no `cd`, no `claude`, no setup ritual.

This is the full walkthrough referenced from [[Welcome]] step 3.

## Prerequisites

- Microsoft **Windows Terminal** installed (Microsoft Store — usually already on Windows 11).
- [[Git Bash]] installed (step 2 of [[Welcome]]).
- [[Claude Code]] installed and signed in (step 6 of [[Welcome]]).

## Create the profile

1. Open Windows Terminal → click the **▾** dropdown next to the tabs → **Settings**.
2. Left sidebar: **+ Add a new profile** → **New empty profile**.
3. Fill in:
    - **Name** — e.g. `OB_Sample`, or whatever you call your vault.
    - **Command line** — `C:/Program Files/Git/bin/bash.exe -i -l -c "claude; exec bash"`
        - This launches Git Bash, runs `claude`, and falls back to a normal Bash prompt when you exit Claude (instead of closing the tab).
    - **Starting directory** — `%USERPROFILE%\OB\Vault1` (replace with your actual vault path).
    - **Icon** — point at one of the `.ico` files in `config/Icons/` (clawd, gemini, ollama) or generate your own with [[nano banana]].
    - **Tab title** — same as the profile name; keeps tabs labeled when you have several agents running.
4. **Appearance** tab (optional but recommended):
    - **Color scheme** — Solarized Dark or whatever you like.
    - **Font face** — 
    - **Cell height** — `1.4` for a bit of breathing room.
5. Save.

## JSON profile (copy-paste shortcut)

If you would rather edit `settings.json` directly: Settings → bottom-left gear → **Open JSON file**, then drop this object into the `"profiles" → "list"` array. Replace `Vault1`, the `guid`, and the icon path.

```json
{
    "name": "OB_Sample",
    "tabTitle": "OB_Sample",
    "guid": "{REPLACE-WITH-A-NEW-GUID}",
    "commandline": "\"C:/Program Files/Git/bin/bash.exe\" -i -l -c \"claude; exec bash\"",
    "startingDirectory": "%USERPROFILE%/OB/Vault1",
    "icon": "%USERPROFILE%/OB/Vault1/config/Icons/clawd.ico",
    "colorScheme": "Solarized Dark",
    "cursorColor": "#CCCCCC",
    "font": {
        "face": "JetBrainsMono Nerd Font",
        "size": 14,
        "cellHeight": "1.4"
    },
    "padding": "8,8,4,8",
    "snapOnInput": false,
    "hidden": false,
    "experimental.repositionCursorWithMouse": true,
    "experimental.retroTerminalEffect": false
}
```

> [!tip] Generating a GUID
> In Git Bash: `python -c "import uuid; print('{' + str(uuid.uuid4()) + '}')"` — or just let Windows Terminal create the profile via the GUI and copy the GUID it assigns.

## Desktop shortcut

You can launch the profile directly from the desktop (or pin to taskbar / Start) without opening Windows Terminal first:

1. Right-click the desktop → **New → Shortcut**.
2. Target: `wt.exe -p "OB_Sample"` (use the exact profile name).
3. Name the shortcut whatever you like.
4. Right-click → **Properties → Change Icon** → point at the same `.ico` you used in the profile.

Now double-clicking the shortcut drops you into a Claude session inside your vault.

## Multiple harnesses (and multiple vaults)

The bigger payoff: duplicate the profile once per **CLI harness** you want a one-click entry for. Same vault, different agent. Swap the binary in `commandline`, swap the icon, give it a name, done.

| Harness     | Command line                                                                     | Icon                                     |
| ----------- | -------------------------------------------------------------------------------- | ---------------------------------------- |
| Claude Code | `"C:/Program Files/Git/bin/bash.exe" -i -l -c "claude; exec bash"`               | `config/Icons/clawd.ico`                 |
| Gemini CLI  | `"C:/Program Files/Git/bin/bash.exe" -i -l -c "gemini; exec bash"`               | `config/Icons/gemini.ico`                |
| Ollama      | `"C:/Program Files/Git/bin/bash.exe" -i -l -c "ollama launch claude; exec bash"` | `config/Icons/ollama.ico`                |
| Pi Agent    | `"C:/Program Files/Git/bin/bash.exe" -i -l -c "pi; exec bash"`                   | (custom — generate with [[nano banana]]) |
| Codex CLI   | `"C:/Program Files/Git/bin/bash.exe" -i -l -c "codex; exec bash"`                | (custom)                                 |
| Plain Bash  | `"C:/Program Files/Git/bin/bash.exe" -i -l`                                      | (none / vault icon)                      |
| Copilot CLI |                                                                                  |                                          |
|             |                                                                                  |                                          |

Each one gets its own desktop shortcut via `wt.exe -p "<profile name>"`, so you can pin Claude, Gemini, Ollama, and Pi side-by-side on the taskbar and launch any of them straight into the vault.

You can also duplicate per **vault** — same harness, different `startingDirectory` — if you keep more than one vault on disk. Most people end up wanting more harnesses than vaults.
