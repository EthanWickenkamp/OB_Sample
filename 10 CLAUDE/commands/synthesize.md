---
description: Read notes, synthesize into the densest paragraph(s) that capture the thesis, then reflect on structure.
argument-hint: note paths or folder — and optionally a focus question
allowed-tools: Read, Edit, Write, Glob, Grep, Bash
---

Read a set of notes and write a dense synthesis. $ARGUMENTS: note paths, folder path, or wikilink names — optionally followed by `>` and a focus question (e.g. `04 Notes/<folder> > where is this headed`).

Think as deeply and as long as you need before writing. Do not rush to output.

---

## Step 1: Parse arguments

Split on `>`:
- **Left side** — one or more note paths, folder paths, or note names to read
- **Right side** (optional) — focus question or angle. If omitted, synthesize the full body of what the notes say together.

Resolve paths:
- If a folder, read all `.md` files in it (non-recursive unless the user says otherwise)
- If note names, find them with Glob/Grep
- Read every resolved note

---

## Step 2: Think

Before writing anything, internalize the full content. Identify:
- What is the **thesis** — the single most important thing these notes say together that none of them says alone?
- What is the **trajectory** — where is this body of work headed?
- What is **latent** — what's implied across the notes but never stated explicitly?

If there's a focus question, orient around it. If not, find the natural center of gravity.

---

## Step 3: Write

Write the densest paragraph you can that captures the thesis. **Start with one paragraph.** Then ask yourself: does this paragraph simultaneously capture the thesis AND leave something load-bearing unsaid? If yes, write the next paragraph — but only the one that covers what's missing. Repeat until the thesis is complete. Stop the moment adding another paragraph would be elaboration rather than completion.

Each paragraph must depend on the one before it. No paragraph should be removable without breaking the argument.

**Style:**
- Information-dense. No filler, no hedging, no "it's worth noting that."
- Concrete. Reference specific notes, specific decisions, specific values by name.
- Assertive. These are conclusions, not suggestions.

---

## Step 4: Reflect

After the synthesis, add a mini heading (`###`) and a short paragraph explaining why you chose the structure you did — how many paragraphs, what each one does, why that number was necessary. This is part of the output, not an aside.

---

## Step 5: Place

Ask the user where to put the output if not obvious. If they've already indicated a file current working note, append it there under a new `##` heading derived from the focus question or thesis.
