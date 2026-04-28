# Home

```button
name 📅 Daily Note
type command
action Daily notes: Open today's daily note
color blue
```

```button
name 💡 New Idea
type note(New Idea) template
action Idea
folder 04 Ideas
prompt true
color green
```

```button
name 💎 New Crystal
type note(New Crystal) template
action Crystal
folder 05 Crystal
prompt true
color purple
```

```button
name 📇 Index
type link
action obsidian://open?vault=OB_Sample&file=05%20Crystal%2FMenus
color default
```

## Pinned

- [[Welcome]]
- [[TODO]]
- [[10 CLAUDE/CLAUDE|CLAUDE]]

## Topic Maps

```dataview
LIST
FROM "05 Menus"
SORT file.name ASC
```

## Recently Edited

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
WHERE file.name != "untitled"
  AND !startswith(file.path, "02 Calendar/")
  AND !startswith(file.name, "MOC")
SORT file.mtime DESC
LIMIT 10
```
