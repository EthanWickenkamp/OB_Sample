---
tags:
  - moc
created: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title.replace(/^MOC_/, "") %>

## Purpose
One line: what this folder is for and what kind of notes it contains

## Recent Activity

```dataview
TABLE
  choice(
    dur(date(now) - file.mtime).hours < 24,
    round(dur(date(now) - file.mtime).hours, 1) + " hours ago",
    choice(
      dur(date(now) - file.mtime).days < 7,
      round(dur(date(now) - file.mtime).days, 1) + " days ago",
      dateformat(file.mtime, "MMM dd")
    )
  ) as "Last Modified"
FROM "FOLDER_PATH"
WHERE file.name != "untitled"
SORT file.mtime DESC
LIMIT 10
```

## Index

### Subfolder
#### Nested Subfolder
- [[Note]] — description
