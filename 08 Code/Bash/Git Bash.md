## Git Bash — Version Control Terminal

Git Bash gives you Git + a Unix-like terminal on Windows. Two things in one package:

### What it is

- **Git** — tracks every change to your files so you can undo, branch, and collaborate
- **Bash** — a Unix shell (the `ls`, `cd`, `grep`, `cat` commands) that normally only exists on Linux/Mac.

On Windows, the default terminal is PowerShell/CMD. Git Bash gives you the (better) commands that every tutorial and Stack Overflow answer assumes you have. 
**Most importantly LLMs are going to be more consistent and better with Bash.**

---

### Why it's useful

| Without Git Bash | With Git Bash |
|---|---|
| No version control — one wrong save and work is gone | Every change is saved, you can rewind to any point |
| PowerShell syntax differs from most tutorials | Bash commands match 90% of online examples |
| No `ssh`, `curl`, `grep` on Windows by default | All included out of the box |

---

### Install

1. Download from [git-scm.com](https://git-scm.com)
2. Run installer — defaults are fine for most people
3. Open "Git Bash" from Start menu

That's it. You now have `git` and a Bash terminal.

---

### Core concepts (the absolute basics)

```bash
# Set up your identity (once, ever)
git config --global user.name "Your Name"
git config --global user.email "you@email.com"

# Start tracking a folder
git init

# Save a snapshot of your current files
git add .
git commit -m "describe what changed"

# See what's changed since last save
git status
git diff

# Undo last commit (keeps your files, just un-commits)
git reset --soft HEAD~1
```

#### The mental model

```
Working Directory  →  git add  →  Staging Area  →  git commit  →  History
(your files)          (picked)      (ready)          (saved)       (permanent)
```

- **Working directory** — your actual files on disk
- **Staging area** — files you've picked to include in the next save
- **History** — the chain of all past commits, rewindable

---

### Common workflows

#### Clone someone else's project
```bash
git clone https://github.com/user/repo.git
cd repo
```

#### Create a branch (experiment without breaking main)
```bash
git checkout -b my-experiment
# make changes...
git add .
git commit -m "tried something"

# go back to main
git checkout main
```

#### Push to GitHub
```bash
# Link to remote (once)
git remote add origin https://github.com/user/repo.git

# Push
git push -u origin main
```

---

### Git Bash vs other terminals

| Tool | What it is |
|---|---|
| **Git Bash** | Git + Bash bundled for Windows. Lightweight, just works |
| **WSL** | Full Linux inside Windows. Heavier, but gives you `apt`, full Linux toolchain |
| **PowerShell** | Windows-native. Different syntax (`Get-ChildItem` instead of `ls`) |
| **Windows Terminal** | Just a window — can run any of the above inside it |

> [!tip] If you're on Linux or Mac
> You already have Bash. Just install Git with your package manager (`apt install git`, `brew install git`) and skip Git Bash entirely — it's a Windows solution.
