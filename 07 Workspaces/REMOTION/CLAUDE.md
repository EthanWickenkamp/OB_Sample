# CLAUDE.md -- Remotion Workspace

This workspace is for developing data-driven video assets using Remotion (React).

## Workspace Purpose
Automate video production for technical explainers and social media by turning scripts (JSON/Markdown) into visual sequences.

## Technology Stack
- **Framework**: Remotion (React + TypeScript)
- **Node.js**: Use `nvm` to manage versions (Target: Node 18+)
- **Build Tool**: Webpack (Internal to Remotion)
- **Preview**: Remotion Player (Browser-based)

## Directory Structure
- `src/` - React components and composition definitions
- `compositions/` - Top-level video layouts
- `assets/` - Images, fonts, and icons
- `specs/` - JSON data driving the video (e.g., subtitles, timestamps)
- `renders/` - Output MP4/PNG files

## Core Commands
```bash
# Preview
npm start                      # Open Remotion Player in browser

# Render
npx remotion render src/index.ts [ID] out/video.mp4

# Snapshots
npx remotion still src/index.ts [ID] out/frame.png --frame [N]
```

## Coding Standards
1. **Deterministic Logic**: Never use `Math.random()` or `Date.now()`. Use `frame` from `useCurrentFrame()` and `interpolate()` for all timing.
2. **Composition Config**:
   - FPS: 30 (Default)
   - Resolution: 1920x1080 (HD) or 1080x1920 (Social)
3. **Naming**:
   - Components: PascalCase (e.g., `HeroScene.tsx`)
   - Composition IDs: kebab-case (e.g., `explainer-video`)
4. **Modularity**: Break scenes into smaller functional components. Use `<Sequence>` to handle temporal placement.

## Integration
Input scripts should be placed in `specs/` as JSON. The main composition should read these to generate the video content dynamically.
