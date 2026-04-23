## Remotion — Video as Code (React)

Remotion lets you create videos using React. Instead of a timeline in a GUI, you use components, hooks, and code to describe your video.

### What it is

- **A framework** — Use React to build components that represent video frames.
- **A renderer** — Uses Puppeteer to browse your React app and capture frames as images, then stitches them into an MP4.
- **A player** — A local browser-based GUI to preview your animations in real-time.

---

### Why it's useful

| Traditional Video Editing | Remotion |
|---|---|
| Manual, hard to version control | Code-driven, perfect for Git |
| Changes require manual rework | Change a prop, re-render automatically |
| Hard to automate at scale | Programmatic video generation (APIs) |
| Proprietary file formats (.prproj, .aep) | Standard .tsx, .json, .css files |

---

### Install

Remotion requires Node.js. Since we use `nvm`, ensure you are on a modern version (Node 18+).

```bash
# Create a new project (interactive)
npx create-remotion@latest

# Or in an existing project
npm install remotion @remotion/cli
```

Verify with:
```bash
npx remotion --version
```

---

### Core Concepts

#### 1. Compositions
The "entry point" of your video. It defines the dimensions, duration (in frames), and FPS.

```tsx
<Composition
  id="MyVideo"
  component={MyComponent}
  durationInFrames={120}
  fps={30}
  width={1920}
  height={1080}
/>
```

#### 2. The `useCurrentFrame` Hook
The heartbeat of Remotion. It returns the current frame number (0 to durationInFrames - 1).

```tsx
const frame = useCurrentFrame();
const opacity = interpolate(frame, [0, 20], [0, 1]); // Fade in over 20 frames
```

#### 3. Sequences
Used to time when components appear and for how long.

```tsx
<Sequence from={30} durationInFrames={60}>
  <MyComponent />
</Sequence>
```

---

### Core Commands

```bash
# Start the preview player (GUI)
npm start

# Render the video to MP4
npx remotion render src/index.ts MyVideo out/video.mp4

# Render a single frame as an image
npx remotion still src/index.ts MyVideo out/frame.png --frame 50
```

---

### The Mental Model

```
React Logic  →  Puppeteer  →  Frame Capture  →  FFmpeg  →  MP4 Video
(Your code)     (Headless)     (.png files)     (Stitch)   (Final Output)
```

- **Frames, not Seconds**: Everything is calculated by frame number. Time = `frame / fps`.
- **Deterministic**: Your code must produce the exact same output for the same frame number every time. No `Math.random()` or `Date.now()` without a seed.

---

### Remotion vs Traditional Tools

| Tool | Strengths | Best For |
|---|---|---|
| **After Effects** | Visual effects, complex masking, GPU acceleration | High-end VFX, artistic motion graphics |
| **Remotion** | Data-driven video, dynamic text, automation, developer familiarity | Technical explainers, social media templates, SaaS demos |
| **Canva** | Easy, templates, no code | Quick social posts, non-technical users |

> [!tip] Integration with this Vault
> Use Remotion in the `07 Workspaces/REMOTION` folder to build visual assets for the `Content Pipeline`. Script logic from `script-lab` can be passed as JSON props to Remotion compositions.
