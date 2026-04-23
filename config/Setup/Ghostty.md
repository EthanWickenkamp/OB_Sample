# Ghostty

A fast, GPU-accelerated terminal emulator with native UI on each platform. Optional terminal upgrade referenced from [[Welcome]] step 4.

Docs: <https://ghostty.org/docs>

## What it is

Ghostty is a modern terminal emulator built around three ideas:

- **Platform-native UI** — uses each OS's native window chrome, tabs, and shortcuts instead of a generic cross-platform shell. Feels like a real Mac/Linux app.
- **GPU acceleration** — fast scrolling, smooth rendering, no lag in big diffs or long agent transcripts.
- **Zero config to start** — sensible defaults, hundreds of built-in themes, light/dark mode auto-switching. You can use it for months without touching a config file.

## Why use it

- Cleaner rendering and smoother scrolling than macOS Terminal or default Linux terminals.
- Built-in themes and font handling — no need to wrestle with profiles to get a nice look.
- Custom keybindings and splits when you do want to dig in.
- Pairs well with Claude Code, Gemini, Codex, Pi, and other CLI agents — especially when you want multiple agent panes side-by-side.

## Install

- **macOS** — download the binary from <https://ghostty.org/download> and drag to `/Applications`.
- **Linux** — packages for most major distros, or build from source. See the docs.
- **Windows** — not officially supported as of writing. Stick with [[Windows Terminal]] on Windows; revisit if/when a native build ships.

## Basics

- First run: it just works. No config file required.
- To customize: drop a config file at `~/.config/ghostty/config` (Linux) or `~/Library/Application Support/com.mitchellh.ghostty/config` (macOS).
- Format is plain `key = value`, one per line. Run `ghostty +show-config --default --docs` to see every option with inline documentation.
- Common starting tweaks: `theme`, `font-family`, `font-size`, `background-opacity`, `keybind`.

## When to skip it

If you are on Windows, Ghostty is not for you yet — use [[Windows Terminal]]. If you do not spend serious time at the terminal, the built-in macOS/Linux terminal is fine. Ghostty is an upgrade, not a requirement.
