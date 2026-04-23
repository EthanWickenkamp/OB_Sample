---
title: Wiki
tags: [index, wiki]
---

# Wiki

The Wiki is the **distilled, stable reference layer** of the vault. Notes here are the things you know to be true and want Claude to treat as authoritative context.

## Wiki vs. Notes vs. Raw Sources

| Layer | Purpose | Mutability |
| --- | --- | --- |
| `01 Raw Sources/` | Captured inputs — articles, PDFs, transcripts, clippings | Immutable — keep as ingested |
| `04 Notes/` | Working thoughts, drafts, project notes, in-progress synthesis | Changes constantly |
| `03 Wiki/` | Distilled, cross-referenced reference notes you return to | Stable, curated, updated deliberately |

Think of it as the "published" shelf. A note collects your interpretations and reasoning behind sources you add. Documentation managed by an agent to allow for knowledge graph and real connections of context. More meaningful than semantic search.

## What belongs here

- Domain concepts you've nailed down and want Claude to reference consistently
- How-I-actually-do-X workflow notes (your personal canonical version)
- Glossaries, cheatsheets, opinionated summaries of a topic, **reasoning**
- Wiki-style entries on tools, people, places, systems that you reference repeatedly
- Im not sure yet the wiki should be agent managed or augmented.
- There is a lot of people researching this still and other good sources available.

## Organization

Organize by topic folder. Each topic is a small self-contained sub-wiki.

- `Obsidian/` — how this vault and Obsidian itself work (the meta-layer)
- *(add folders as domains crystallize)*

## How to promote a note

1. A note in `04 Notes/` has been rewritten, linked, and used enough that you trust it.
2. Decide what topic folder it belongs in (create one if needed).
3. Use `/move` to relocate it — wikilinks auto-update.
4. Trim anything tentative. Wiki notes should read like reference, not like thinking-out-loud.
5. Add it to the relevant topic index, if there is one.

## Wiki ↔ Crystal Notes

If you come from a "Crystal Notes" setup, the Wiki is the same idea: the final, crystallized reference layer. The `/crystal` command promotes a note from rough to reference — use it to populate this folder.
