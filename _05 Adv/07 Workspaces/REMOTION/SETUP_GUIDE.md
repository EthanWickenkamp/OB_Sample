# Remotion Workspace Setup Guide

## What This Is

[Remotion](https://www.remotion.dev/) is a framework for making videos programmatically with React and TypeScript. You write video compositions as React components, preview them in a browser, and render to MP4/PNG. This workspace uses it to automate video production — technical explainers, social media clips, data-driven visuals.

## Why It Matters for This Vault

The Content Pipeline workspace (`07 Workspaces/Content Pipeline/`) handles scripts and distribution. Remotion is the rendering engine — it turns those scripts (as JSON in `specs/`) into actual video files. Claude can help write compositions, debug animations, and generate spec files.

## Prerequisites

- **Node.js 18+** (required for Remotion v4/v5)
- **npm** (comes with Node)

That's it. Works on Windows, Mac, and Linux.

### Install Node.js if needed

- **Windows/Mac:** Download from [nodejs.org](https://nodejs.org/) (LTS recommended), or use `nvm`
- **Mac (Homebrew):** `brew install node`
- **Linux:** `sudo apt install nodejs npm` or use [nvm](https://github.com/nvm-sh/nvm)

Verify: `node --version` (should be 18+)

## Setup

From this directory (`07 Workspaces/REMOTION/`):

```bash
npm install
```

That installs all dependencies from `package.json`. Takes a minute or two.

## Usage

```bash
# Preview in browser (live reload)
npm start

# Render a video
npx remotion render src/index.ts [CompositionID] out/video.mp4

# Render a single frame
npx remotion still src/index.ts [CompositionID] out/frame.png --frame [N]
```

## Starting from scratch (alternative)

If you'd rather start fresh instead of using this workspace's existing setup:

```bash
npx create-video@latest
```

This scaffolds a new Remotion project with templates to choose from.

## Directory Structure

```
REMOTION/
  src/              React components and composition definitions
  compositions/     Top-level video layouts
  assets/           Images, fonts, icons
  specs/            JSON data driving videos (subtitles, timestamps)
  renders/          Output MP4/PNG files
  CLAUDE.md         Development context for Claude
  SETUP_GUIDE.md    This file
```

## Important

- `node_modules/` is not included — run `npm install` to generate it
- Do not commit or sync `node_modules/` (it's ~700MB of dependencies)
- See `CLAUDE.md` in this folder for coding standards and Remotion-specific rules

---
**References:**
- [Remotion Docs](https://www.remotion.dev/docs/)
- [Remotion GitHub](https://github.com/remotion-dev/remotion)
