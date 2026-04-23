## Bun — JavaScript Runtime & Package Manager

Bun replaces Node.js, npm, and bundlers in one tool. It runs JavaScript/TypeScript fast.

### What it is

- A **runtime** — runs `.js` and `.ts` files directly (like Node, but faster)
- A **package manager** — installs packages (like npm/yarn, but much faster)
- A **bundler** — combines files for production (like webpack, but built-in)

One binary does what used to take 3-4 separate tools.

---

### Why it's useful

| Without Bun (traditional) | With Bun |
|---|---|
| Install Node + npm separately | One install |
| `npm install` takes 30+ seconds | `bun install` often takes 2-3 seconds |
| Need TypeScript compiler to run `.ts` | Runs `.ts` natively, no config |
| Need webpack/vite for bundling | `bun build` is built in |

---

### Install

```bash
# Linux / Mac / WSL
curl -fsSL https://bun.sh/install | bash

# Windows (native, experimental)
powershell -c "irm bun.sh/install.ps1 | iex"
```

Restart your terminal after install. Verify with:
```bash
bun --version
```

---

### Core usage

```bash
# Run a script (JS or TS, no config needed)
bun run script.ts

# Start a project
bun init

# Install all dependencies from package.json
bun install

# Add a package
bun add <package>

# Remove a package
bun remove <package>

# Run a script defined in package.json
bun run dev
```

---

### The mental model

```
bun = Node.js  +  npm  +  tsc  +  bundler
      (runtime)  (packages) (TypeScript) (build)
```

- Drop-in replacement for Node in most cases
- Reads the same `package.json` and `node_modules/` that npm uses
- If a project works with Node/npm, it usually works with Bun

---

### Bun vs Node vs Deno

| Tool | Strengths | Trade-offs |
|---|---|---|
| **Node.js** | Biggest ecosystem, most stable, universal support | Slower, needs separate TypeScript setup |
| **Bun** | Fastest, all-in-one, npm-compatible | Newer, some edge cases don't match Node exactly |
| **Deno** | Security-first, TypeScript native | Different module system, smaller ecosystem |

> [!tip] When to use Bun
> Good default for new projects and scripts. For production apps that need maximum compatibility, Node is still the safe choice.
