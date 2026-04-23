# NotebookLM Workspace

NotebookLM is a scoped research assistant for heavy source digestion. Use it to chew through large PDFs, papers, and transcripts that would be expensive to run through Claude directly — then pull the distilled output back into the vault.

See [[SETUP_GUIDE]] for the full rationale and feature breakdown.

## Workflow

1. Drop raw sources (PDFs, YouTube links, web pages) into a NotebookLM notebook.
2. Generate one of: Study Guide, FAQ, Timeline, Briefing Doc, Audio Overview.
3. Export the output as markdown and save it to `01 Raw Sources/` with a link back to the NotebookLM notebook URL.
4. Ask Claude to crystallize the distilled version into `03 Wiki/` or a topic note in `04 Notes/`.

## Rules

- Do not ask Claude to summarize a 50+ page PDF directly — route it through NotebookLM first.
- Always capture the NotebookLM notebook URL in the frontmatter of any imported note so the source chain stays traceable.
- Audio overviews are for review/commute — transcribe only if a specific insight is worth crystallizing.

## Routing

| Task | Go to |
| --- | --- |
| Import a new source set | NotebookLM → export → `01 Raw Sources/` |
| Distill into a vault note | `04 Notes/` or `03 Wiki/` |
| Link related imports | `05 Menus/` (build a MOC) |
