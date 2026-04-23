---
title: "Obsidian Commands"
source: "https://internetvin.com/Obsidian+Commands"
author:
  - "[[Vin]]"
published:
created: 2026-03-13
description: "Index - Vin"
tags:
  - "clippings"
---
These are the commands that I currently use when I am using [Obsidian](https://internetvin.com/Obsidian) with [Claude Code](https://internetvin.com/Claude+Code), or any agent.

These commands work most effectively if you have the [Obsidian CLI](https://help.obsidian.md/cli) installed. Some of them also require connections to other MCPs like Google Calendar, Google Tasks, and GMail. You can obviously adjust that however you would like.

Every command runs against an Obsidian vault with daily notes, context files, and linked thinking. The agent reads the vault in real time, every time.

I have removed personal details from these prompts. You should play with them and modify them to suit your own preferences, accounts, and information.

## Vault Commands

| Command | What It Does | Prompt |
| --- | --- | --- |
| `/context` | Reads across the vault to build a full picture of who you are, what you're working on, and what you care about right now | [Prompt - Context](https://internetvin.com/Prompts/Prompt+-+Context) |
| `/today` | Pulls from recent notes, calendar, and open threads to generate a daily plan grounded in what's actually happening | [Prompt - Today](https://internetvin.com/Prompts/Prompt+-+Today) |
| `/close-day` | Reviews what happened today, captures what you learned, and flags anything unresolved for tomorrow | [Prompt - Close Day](https://internetvin.com/Prompts/Prompt+-+Close+Day) |
| `/schedule` | Schedules events by reading your priorities, commitments, and energy patterns from the vault, not just calendar gaps | [Prompt - Schedule](https://internetvin.com/Prompts/Prompt+-+Schedule) |
| `/7plan` | Looks at what's most alive in your thinking right now and reshapes the next 7 days around it | [Prompt - 7plan](https://internetvin.com/Prompts/Prompt+-+7plan) |
| `/map` | Generates a topological view of everything in the vault, showing clusters, themes, and how ideas relate | [Prompt - Map](https://internetvin.com/Prompts/Prompt+-+Map) |
| `/ghost` | Answers any question as you by reading your notes, beliefs, and writing style from the vault | [Prompt - Ghost](https://internetvin.com/Prompts/Prompt+-+Ghost) |
| `/trace` | Takes an idea and tracks how your thinking about it changed over weeks or months through daily notes | [Prompt - Trace](https://internetvin.com/Prompts/Prompt+-+Trace) |
| `/emerge` | Finds ideas you've never explicitly written but that are strongly implied by patterns across multiple notes | [Prompt - Emerge](https://internetvin.com/Prompts/Prompt+-+Emerge) |
| `/connect` | Surfaces unexpected bridges between unrelated domains in the vault that you haven't noticed | [Prompt - Connect](https://internetvin.com/Prompts/Prompt+-+Connect) |
| `/contradict` | Finds places where you hold two incompatible beliefs at the same time across different notes | [Prompt - Contradict](https://internetvin.com/Prompts/Prompt+-+Contradict) |
| `/drift` | Identifies topics, projects, or commitments you've been quietly avoiding based on gaps in your notes | [Prompt - Drift](https://internetvin.com/Prompts/Prompt+-+Drift) |
| `/challenge` | Reads your current thinking on a topic and argues against it using evidence from your own vault | [Prompt - Challenge](https://internetvin.com/Prompts/Prompt+-+Challenge) |
| `/stranger` | Reads the entire vault and writes a portrait of you as if from someone who's never met you | [Prompt - Stranger](https://internetvin.com/Prompts/Prompt+-+Stranger) |
| `/compound` | Asks the same question at different points in time across the vault to show how context compounds | [Prompt - Compound](https://internetvin.com/Prompts/Prompt+-+Compound) |
| `/backlinks` | Finds notes that should be linked but aren't and wires new connections across the vault | [Prompt - Backlinks](https://internetvin.com/Prompts/Prompt+-+Backlinks) |
| `/graduate` | Extracts ideas buried in daily notes and promotes them into standalone permanent notes | [Prompt - Graduate](https://internetvin.com/Prompts/Prompt+-+Graduate) |
| `/xdaily` | Pulls X/Twitter posts and threads them into the relevant daily notes | [Prompt - XDaily](https://internetvin.com/Prompts/Prompt+-+XDaily) |
| `/ideas` | Generates new ideas by reading current projects, interests, and open questions across the vault | [Prompt - Ideas](https://internetvin.com/Prompts/Prompt+-+Ideas) |
| `/learned` | Turns recent learnings from the vault into a polished "What I Learned" post | [Prompt - Learned](https://internetvin.com/Prompts/Prompt+-+Learned) |
| `/weekly-learnings` | Compiles the week's insights from daily notes into a single writing-ready summary | [Prompt - Weekly Learnings](https://internetvin.com/Prompts/Prompt+-+Weekly+Learnings) |
| `/make` | Finds ideas in the vault that have matured enough to become something real, scores their readiness, and suggests what form each could take | [Prompt - Make](https://internetvin.com/Prompts/Prompt+-+Make) |
| `/money` | Reads the vault to surface how you could be making money, diagnoses what's broken in your revenue system, and recommends specific opportunities | [Prompt - Money](https://internetvin.com/Prompts/Prompt+-+Money) |
| `/guests` | Derives who you should be talking to on the show by starting from questions the vault is actively asking, not from a guest pipeline | [Prompt - Guests](https://internetvin.com/Prompt+-+Guests) |
| `/leverage` | Scans the vault to find the 3-7 skills, knowledge domains, or mental models where concentrated investment would produce disproportionate breakthroughs across multiple domains simultaneously | [Prompt - Leverage](https://internetvin.com/Prompts/Prompt+-+Leverage) |
| `/xarticle` | Scans the vault for topics with graph density, current energy, and synthesis potential to find what to write for the next X Article | [Prompt - XArticle](https://internetvin.com/Prompt+-+XArticle) |