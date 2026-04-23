## uv — Python Package Manager

uv replaces `pip`, `venv`, and `pyenv` in one tool. This vault uses it to manage a single consolidated Python environment that every Claude Code skill shares.

### What it is

- A **package manager** — installs Python packages (like pip, but much faster)
- An **environment manager** — creates isolated venvs (like `python -m venv`)
- A **Python installer** — downloads and manages Python versions (like pyenv)

One binary does what used to take three separate tools.

---

### Install

```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux / Mac / WSL
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Restart your terminal, then verify:

```bash
uv --version
```

---

### The consolidated `claude` venv

This vault can use **one** persistent venv that every Python-using skill in `.claude/` points at:

**Path:** `~/.venvs/claude/` (Python 3.14)

Why one venv instead of many:

- Every skill shares the same interpreter and library versions — no per-skill "which env am I in?"
- One `PYTHONUTF8=1` + one interpreter path, so [[Claude Code]] skills stay simple
- Easy to rebuild: delete the folder, reinstall from the list below, done

Create it once:

```bash
uv venv "$HOME/.venvs/claude" --python 3.14
```

Then install libraries into it (see list below).

> [!note] Windows paths
> On Windows the interpreter lives at `$HOME/.venvs/claude/Scripts/python.exe`. On Linux/Mac it's `$HOME/.venvs/claude/bin/python`. Always call the venv's python directly — never bare `python`.
>
> Prefix PDF or OCR work with `PYTHONUTF8=1` on Windows to avoid encoding errors.

```bash
# Windows
"$HOME/.venvs/claude/Scripts/python.exe" -c "import pandas; print(pandas.__version__)"

# Linux / Mac
"$HOME/.venvs/claude/bin/python" -c "import pandas; print(pandas.__version__)"
```

---

### Installed libraries and what they do

These are the packages the vault's Claude Code skills rely on. Each one unlocks a category of work Claude can do against your notes.

#### Document processing

| Library | Purpose | Typical use in the vault |
|---|---|---|
| **`pymupdf4llm`** | Converts PDFs to clean Markdown structured for LLMs | Turning PDFs in `01 Raw Sources/` into readable notes |
| **`pdfplumber`** | Alternative PDF extractor, much better at tables than `pymupdf4llm` | Use when a PDF is table-heavy; pick per document |
| **`python-doctr`** | OCR for scanned documents and images (deep-learning based) | Extracting text from scans or screenshots `pymupdf4llm` can't read |
| **`python-docx`** | Reads and writes `.docx` Word documents | Importing Word docs into notes, or exporting notes to Word |
| **`python-pptx`** | Reads and writes `.pptx` PowerPoint files | Pulling slides into course notes |
| **`openpyxl`** | Reads and writes `.xlsx` Excel files | Parsing spreadsheets dropped into the vault |
| **`pypandoc_binary`** | Python wrapper around Pandoc (bundles pandoc itself, no separate install) | Converting between Markdown ↔ DOCX, HTML, LaTeX, etc. |

#### Web and media

| Library | Purpose | Typical use in the vault |
|---|---|---|
| **`httpx`** | Modern async-capable HTTP client | Any skill that fetches URLs, downloads files, or calls APIs |
| **`beautifulsoup4`** | HTML/XML parser | Cleaning `Clippings/` web pages, extracting content from raw HTML |
| **`markdownify`** | HTML → Markdown conversion | Pairs with `beautifulsoup4` to turn scraped pages into paste-ready notes |
| **`youtube-transcript-api`** | Fetches YouTube captions by video ID — no API key | `/youtube-transcript` skill, pulling transcripts into `01 Raw Sources/` |
| **`yt-dlp`** | Downloads YouTube audio/video when captions aren't enough | Fallback for videos without transcripts (pipe audio to whisper) |

#### Data and imaging

| Library | Purpose | Typical use in the vault |
|---|---|---|
| **`pandas`** | DataFrame library for tabular data | Summarizing CSVs, Excel sheets, or markdown tables |
| **`matplotlib`** | Plotting and charting | Generating charts from vault data and saving them to `00 Attachments/` |
| **`pillow`** | Image manipulation (resize, crop, convert) | Normalizing images in `00 Attachments/`; also a transitive dep of `python-doctr` |

#### Vault and LLM tooling

| Library | Purpose | Typical use in the vault |
|---|---|---|
| **`python-frontmatter`** | Reads and edits YAML frontmatter in Markdown files | Any skill that touches note properties (tags, dates, title) |
| **`tiktoken`** | Token counting for OpenAI-style tokenizers | Estimating whether a chunk of notes will fit in a model's context |

Install them all at once:

```bash
PY="$HOME/.venvs/claude/Scripts/python.exe"   # Windows
# PY="$HOME/.venvs/claude/bin/python"          # Linux / Mac

uv pip install --python "$PY" \
  pymupdf4llm pdfplumber python-doctr python-docx python-pptx openpyxl pypandoc_binary \
  httpx beautifulsoup4 markdownify youtube-transcript-api yt-dlp \
  pandas matplotlib pillow \
  python-frontmatter tiktoken
```

---

### Adding a new library

When a new skill needs a Python package, add it to the consolidated venv (don't make a new one):

```bash
uv pip install <package> --python "$HOME/.venvs/claude/Scripts/python.exe"
```

Then update both:

1. This note's library table
2. The `## Python` section of `10 CLAUDE/CLAUDE.md` (keep the two lists in sync)

---

### Ephemeral use (one-off scripts, no venv)

For quick throwaway experiments that shouldn't pollute the shared venv:

```bash
uv run --with <package> python -c "..."
```

- Downloads the package into a cached temp env, runs the command, exits
- Cache persists so repeat runs are fast
- Fine for exploring; not for skills the vault depends on

---

### Verifying the environment (new device or fresh clone)

Run through this checklist if you're setting up a new device, or if a skill starts failing on imports. Don't skip steps.

#### Step 1: uv exists

```bash
uv --version
```

If missing, install (see **Install** above).

#### Step 2: venv exists

```bash
ls "$HOME/.venvs/claude/"
```

Should contain `Scripts/` (Windows) or `bin/` (Linux/Mac). If missing, create and install (see **Rebuild from scratch** below).

#### Step 3: Python runs

```bash
"$HOME/.venvs/claude/Scripts/python.exe" --version   # Windows
"$HOME/.venvs/claude/bin/python" --version            # Linux / Mac
```

Should print `Python 3.14.x`. If it errors or shows a different major version, rebuild.

#### Step 4: imports work

```bash
"$HOME/.venvs/claude/Scripts/python.exe" -c "
import pymupdf4llm, pdfplumber, doctr, docx, pptx, openpyxl, pypandoc
import httpx, bs4, markdownify, youtube_transcript_api, yt_dlp
import pandas, matplotlib, PIL
import frontmatter, tiktoken
print('ALL IMPORTS PASSED')
"
```

If any fail, install just the missing one:

```bash
uv pip install <missing-pkg> --python "$HOME/.venvs/claude/Scripts/python.exe"
```

#### Step 5: no stray venvs

```bash
ls "$HOME/.venvs/"
```

Only `claude/` should exist. If you find others, they're stale — remove them so future skills don't accidentally grab the wrong interpreter.

---

### Rebuild from scratch

If the venv is broken beyond repair:

```bash
rm -rf "$HOME/.venvs/claude"
uv venv "$HOME/.venvs/claude" --python 3.14

PY="$HOME/.venvs/claude/Scripts/python.exe"   # Windows
# PY="$HOME/.venvs/claude/bin/python"          # Linux / Mac

uv pip install --python "$PY" \
  pymupdf4llm pdfplumber python-doctr python-docx python-pptx openpyxl pypandoc_binary \
  httpx beautifulsoup4 markdownify youtube-transcript-api yt-dlp \
  pandas matplotlib pillow \
  python-frontmatter tiktoken
```

Then re-run the verification checklist above.

---

### See also

- [[Claude Code]] — the agent that runs skills against this venv
- `10 CLAUDE/CLAUDE.md` — canonical Python section, kept in sync with this note
