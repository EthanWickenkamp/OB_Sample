# NotebookLM Workspace Setup Guide

## What This Is

[NotebookLM](https://notebooklm.google.com) is Google's AI research tool that ingests your sources — PDFs, docs, web pages, YouTube videos — and lets you query, summarize, and generate content from them. Think of it as a scoped research assistant with its own context window, completely separate from Claude.

## Why It Matters for This Vault

NotebookLM and Claude Code serve different roles in your workflow:

| | NotebookLM | Claude Code |
|---|---|---|
| **Strength** | Deep research over large source sets | Vault management, writing, code, structured workflows |
| **Context** | Your uploaded sources (up to 50 per notebook) | Your vault files + conversation |
| **Cost** | Free (Google) | Token-based |
| **Output** | Summaries, podcasts, FAQs, study guides, timelines | Notes, edits, code, organized vault content |

**The connection:** NotebookLM handles the heavy source digestion — reading 200-page PDFs, cross-referencing papers, generating audio overviews. Claude handles the vault side — organizing what comes back, integrating it into your notes, building on it.

### Token savings
Instead of feeding Claude a 50-page PDF and asking for a summary (expensive), upload it to NotebookLM first. Pull the generated summary, key quotes, or FAQ into your vault. Then Claude works with the distilled version.

## Features to Build Around

NotebookLM can generate from your sources:
- **Audio Overviews** — podcast-style conversations about your sources (great for review/commute)
- **Study Guides** — structured summaries with key concepts
- **FAQs** — question-answer pairs extracted from sources
- **Timelines** — chronological event extraction
- **Briefing Docs** — executive-summary style overviews
- **Flashcards** — for active recall study
- **Source-grounded Q&A** — ask questions, get answers with citations to your uploaded docs

## Setting Up the Workspace

### 1. Create notebooks by project or class
Each NotebookLM notebook should map to something in your vault — a class, a research topic, a project. Keep the naming consistent.

### 2. Workspace structure
```
07 Workspaces/NotebookLM/
  SETUP_GUIDE.md          (this file)
  notebooks.md            (index of your notebooks and what sources are in each)
  <topic>/               (one folder per active notebook, for captured output)
```

### 3. Workflow: Source in, notes out
1. Upload source material to a NotebookLM notebook (PDFs, URLs, YouTube links, Google Docs)
2. Use NotebookLM to generate the output type you need (summary, FAQ, podcast, etc.)
3. Copy or transcribe the output into your vault under `01 Raw Sources/` or directly into a project note
4. Use Claude to integrate, refine, or build on the captured content

### 4. Connecting to classes
For each class in `09 Classes/`, consider a matching NotebookLM notebook with:
- Uploaded lecture slides / readings
- Generated study guides before exams
- Audio overviews for review sessions
- FAQ generation from dense readings

## Tips
- NotebookLM works best with **specific, scoped source sets** — don't dump everything into one notebook
- Audio Overviews are surprisingly good for building intuition about a topic before diving into details
- The source-grounded Q&A is more reliable than general LLM chat because it cites specific passages
- You can share notebooks with collaborators — useful for group projects
