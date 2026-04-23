---
name: search-context
description: Search and explore vault — full-text search, tags, links, backlinks, outlines, orphans, unresolved links.
argument-hint: "query or exploration command"
allowed-tools: Bash, Read, Glob, Grep
---

Search and explore the vault to understand how notes relate and gather context before acting. $ARGUMENTS: a search query or exploration goal.

Use your judgment on which commands fit the request. Combine multiple if needed.

## Obsidian CLI search & context reference

```
obsidian search query="..."                    Full-text search (file list)
obsidian search:context query="..."            Full-text search with matching line context
obsidian search query="..." path=<folder> limit=<n>  Scoped and limited search
obsidian tags counts sort=count                All tags with occurrence counts
obsidian tag name=<tag> verbose                Notes containing a specific tag
obsidian links file=<name>                     Outgoing links from a note
obsidian backlinks file=<name>                 Incoming links to a note (add counts for link counts)
obsidian outline file=<name>                   Heading structure (format=tree|md|json)
obsidian orphans                               Notes with no incoming links
obsidian unresolved verbose                    Broken/unresolved wikilinks with source files
```

You can also use Grep and Glob directly for raw file content search when the Obsidian index isn't needed.

Full CLI reference: `config/Obsidian CLI Commands.md`

Ready to add QMD or other semantic search upgrade.