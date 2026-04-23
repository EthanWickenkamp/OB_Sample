## nvm — Node Version Manager

nvm lets you install and switch between multiple versions of Node.js. Node comes bundled with npm, installing Node through nvm gives you both.

### What it is

- A **version manager** — installs any version of Node.js side by side
- Switches versions per terminal session or per project
- Does NOT install globally — everything lives in your home folder (`~/.nvm/`)

---

### Why it's useful

| Without nvm | With nvm |
|---|---|
| One Node version system-wide, upgrades break old projects | Any version per project, switch in one command |
| Uninstalling Node is messy | `nvm uninstall <version>` and it's gone |
| Need admin/sudo to install Node | Installs to your home folder, no permissions needed |

---

### Install

```bash
# Linux / Mac / WSL
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

Restart your terminal, then verify:
```bash
nvm --version
```

> [!note] Windows
> nvm doesn't run on Windows natively. Use [nvm-windows](https://github.com/coreybutler/nvm-windows) instead — similar commands, separate project.

---

### Core usage

```bash
# Install latest LTS (Long Term Support — the safe/stable one)
nvm install --lts

# Install a specific version
nvm install 22

# Switch to a version (this terminal session)
nvm use 22

# See what's installed
nvm ls

# Set a default version (all new terminals)
nvm alias default 22
```

---

### Per-project version

Create a `.nvmrc` file in your project root:
```
20
```

Then anyone can run:
```bash
nvm use
# reads .nvmrc, switches to that version
```

---

## Node.js

Node is a JavaScript runtime — it lets you run JavaScript outside the browser (on your computer, on a server). A browser is a JavaScript runtime.

### What it's for

- **Scripts** — automate tasks, process files, run tools
- **Servers** — build web APIs and backends
- **CLI tools** — most modern dev tools (Vite, ESLint, Prettier) are Node programs

### Core commands

```bash
# Run a JavaScript file
node script.js

# Start a REPL (interactive JS prompt)
node

# Check version
node --version
```

### The mental model

```
Browser JS  →  can access the page (DOM, window, document)
Node JS     →  can access the computer (files, network, processes)
```

Same language, different environment. Code that uses `document.getElementById` won't work in Node. Code that uses `fs.readFile` won't work in the browser.

---

## npm — Node Package Manager

npm installs and manages JavaScript packages (libraries other people wrote). It comes bundled with Node — if you have Node, you have npm.

### What it's for

- **Install packages** — pull in code from the npm registry (1M+ packages)
- **Manage dependencies** — track what your project needs in `package.json`
- **Run scripts** — define shortcuts like `npm run dev`, `npm run build`

### Core commands

```bash
# Start a new project (creates package.json)
npm init -y

# Install a package (adds to package.json + node_modules/)
npm install <package>

# Install all dependencies listed in package.json
npm install

# Remove a package
npm uninstall <package>

# Run a script from package.json
npm run <script-name>

# Install a tool globally (available everywhere)
npm install -g <package>
```

### Key files

| File                | What it is                                                              |
| ------------------- | ----------------------------------------------------------------------- |
| `package.json`      | Your project's manifest — lists dependencies, scripts, metadata         |
| `package-lock.json` | Exact versions of everything installed (commit this)                    |
| `node_modules/`     | The actual downloaded packages (don't commit this, add to `.gitignore`) |

### The mental model
Example package install path

```
npm install express
    ↓
1. Finds "express" in the npm registry
2. Downloads it + all its dependencies
3. Puts them in node_modules/
4. Records the exact versions in package-lock.json
5. Adds "express" to package.json
```

> [!tip] npm vs Bun
> Bun can replace npm for installs (`bun install` is much faster). But npm is the default that every tutorial uses and every project supports. Use npm first, switch to Bun later if specifically supported and speed matters.
[[Bun]]