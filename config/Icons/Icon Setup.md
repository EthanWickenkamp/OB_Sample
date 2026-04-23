# Icon Setup

Configure folder and file icons for the **Icon Folder** plugin (`obsidian-icon-folder`).

Icons are stored in `.obsidian/plugins/obsidian-icon-folder/data.json`. Each entry is a key-value pair:

```
"<folder or file name>": "<emoji or Lucide icon ID>"
```

Lucide icons use the format `Li` + PascalCase name (e.g. `LiCodesandbox`). Browse at [lucide.dev](https://lucide.dev).

---

## Current Assignments

| Path | Icon |
|------|------|
| `HOME.md` | 🏠 |
| `TODO.md` | ✅ |
| `00 Attachments` | 🔗 |
| `01 Raw Sources` | 📰 |
| `02 Calendar` | 📅 |
| `03 Wiki` | ⚓ |
| `04 Ideas` | 🌱 |
| `05 Crystal` | 💎 |
| `07 Workspaces` | ⚒ |
| `08 Code` | `LiCodesandbox` |
| `10 CLAUDE` | 🦧 |
| `11 GEMINI` | ♊ |
| `12 PI` | `LiPi` |
| `13 Codex` | 🌩 |

## Needs Icons

| Path | Purpose | Suggested Icon |
|------|---------|---------------|
| `Clippings` | Saved web clippings | |
| `Inbox` | Drop zone for new notes | |
| `config` | Vault config/templates/scripts | |
| `Welcome.md` | Onboarding note | |

---

## Task for Claude

Fill in the **Suggested Icon** column above, then apply to `data.json`:

1. Open `.obsidian/plugins/obsidian-icon-folder/data.json`
2. Add entries for any missing paths following the existing format
3. Use emojis or `Li`-prefixed Lucide IDs — no other formats work

The `settings` block at the top of `data.json` should not be changed.
