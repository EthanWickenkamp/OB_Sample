# Plugins

Plugin state across both vaults: 18 canonical enabled + 11 evaluation disabled = **29 total community plugins**, OB_Sample. Not sure this is 100% accurate. Suggested list anyway edit however.

---

## Canonical — Enabled (18)

### Core Workflow

| Plugin | Description |
|--------|-------------|
| **Dataview** | Query and display vault data with inline code blocks and tables |
| **Tasks** | Track tasks across the vault with due dates, recurrence, and filtering |
| **Calendar** | Calendar sidebar view of daily notes |
| **Omnisearch** | Full-text search engine with better ranking and indexing |
| **Buttons** | Clickable buttons in notes that run commands, open files, or trigger templates |
| **Git** | Commit, pull, push the vault from inside Obsidian |

### Editing

| Plugin | Description |
|--------|-------------|
| **Advanced Tables** | Improved table navigation, formatting, and formulas — canonical table editor |
| **Excalidraw** | Embedded sketch and diagram editor with visual PKM features |
| **Mind Map** | Convert headings into mind map view |
| **Templater** | Dynamic templates with JS expressions, dates, file-title-driven headings — powers `obsidian create template=` |

### Reading and Export

| Plugin | Description |
|--------|-------------|
| **PDF++** | Native PDF annotation — highlight, annotate, and link to PDF sections |
| **Pandoc Plugin** | Export notes to DOCX, ePub, PDF, and other formats via Pandoc |

### Appearance and Organization

| Plugin | Description |
|--------|-------------|
| **Homepage** | Auto-open a chosen note or workspace on Obsidian launch |
| **Minimal Theme Settings** | Adjust colors, fonts, and features of the Minimal theme |
| **Style Settings** | Fine-tune CSS variables for themes, plugins, and snippets |
| **Iconize** | Add icons to files, folders, and text |
| **Custom Attachment Location** | Route pasted images and files to custom paths using variables |
| **Auto Link Title** | Fetch page title when pasting URLs |

---

## Evaluation — Installed but Disabled (11)

Installed so this vault can flip them on instantly, but not in the active set. See `config/Plugins Comparison.md` in OB_Claude for rationale on each.

| Plugin                  | Status                                                         |
| ----------------------- | -------------------------------------------------------------- |
| **Terminal**            | Embedded shell — external terminal already covers the use case |
| **Local REST API**      | Held for possible future external integrations, CLI pref       |
| **Commander**           | Pending comparison vs Buttons                                  |
| **Custom Sort**         | Pending comparison vs MAKE.md / spaces-style folder plugins    |
| **Obsidian Annotator**  | PDF/EPUB annotation — evaluate side-by-side with PDF++         |
| **Importer**            | One-shot Notion/Evernote/etc. migration tool                   |
| **Colored Tags**        | Tag cluster — evaluate via `/tagger` audit                     |
| **MetaEdit**            | Tag cluster — evaluate via `/tagger` audit                     |
| **Tags Overview**       | Tag cluster — evaluate via `/tagger` audit                     |
| **Tag Wrangler**        | Tag cluster — evaluate via `/tagger` audit                     |
| **Various Complements** | Smarter autocomplete; didn't stick, but complementary          |
