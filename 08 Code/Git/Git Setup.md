## Git Setup — Version Your Vault

Turning your vault into a git repository gives you full history: every change is saved, you can rewind to any version, and you get a safety net for experiments. You have three options depending on how much backup and sync you need.

### Why version your vault

- Undo any accidental delete or edit — even months later
- See a timeline of how your notes evolved
- Optional: off-site backup and sync across machines

All three options start with [[Git Bash]] (or any terminal with `git` installed).

---

### Option 1 — Local git only

The simplest setup. Your vault folder becomes a git repo on your own machine. No account, no remote, nothing to configure beyond git itself.

```bash
cd /path/to/your/vault
git init
git add .
git commit -m "initial vault snapshot"
```

From then on, commit whenever you want a checkpoint:

```bash
git add .
git commit -m "notes from today"
```

**Pros:** zero setup, fully private, works offline.
**Cons:** no off-site backup — if the drive dies, history dies with it. No sync between machines.

> [!tip] Pair with Dropbox?
> If your vault lives in Dropbox (like this one), Dropbox handles cross-machine sync while git handles history. Use them together — just avoid editing from two machines at the same moment.

---

### Option 2 — Self-hosted remote (no GitHub)

Same as Option 1, but you push commits to a "bare" repo on another machine or drive. This gives you off-site backup without depending on any third-party service.

The remote can live on:

- Another computer you own (via SSH)
- An external hard drive or USB stick
- A home server or NAS

```bash
# On the remote machine or drive — create a bare repo
git init --bare /path/to/vault.git

# On your main machine — add it as the remote and push
cd /path/to/your/vault
git remote add origin ssh://user@host/path/to/vault.git
# …or for a local drive path:
# git remote add origin /mnt/external/vault.git
git push -u origin main
```

After that, `git push` backs up and `git pull` syncs on another machine.

**Pros:** fully private, no third-party service, works over any network or drive.
**Cons:** you manage the remote yourself. If the drive dies, your backup dies.

---

### Option 3 — Private GitHub repository

GitHub hosts the remote for you. Private repos are free and visible only to you (and people you explicitly invite).

1. Make a GitHub account at [github.com](https://github.com) if you don't have one.
2. Click **New repository**, give it a name, and select **Private**. Don't initialize with a README — you already have files.
3. Run the commands GitHub shows you on the next screen:

```bash
cd /path/to/your/vault
git init
git add .
git commit -m "initial vault snapshot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

**Pros:** off-site backup, easy multi-machine sync, free, nice web UI for browsing history.
**Cons:** your notes live on GitHub's servers — encrypted, but still a third party.

> [!warning] Sensitive notes
> Even in a private repo, don't store passwords, API keys, or anything you'd never want leaked. Option 1 or 2 is safer for that kind of content.

---

### Which should I pick?

| You want | Use |
|---|---|
| The simplest possible setup | **Option 1** (local) |
| Backup with no third parties | **Option 2** (self-hosted) |
| Backup plus easy multi-device sync | **Option 3** (GitHub private) |

If you're unsure, start with **Option 1** — you can always add a remote later with `git remote add origin …` and push.

---

### See also

- [[Git Bash]] — the terminal you'll run these commands in on Windows
