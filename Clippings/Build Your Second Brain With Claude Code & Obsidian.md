---
title: "Build Your Second Brain With Claude Code & Obsidian"
source: "https://www.whytryai.com/p/claude-code-obsidian"
author:
  - "[[Daniel Nest]]"
published: 2026-02-26
created: 2026-04-01
description: "Your AI context shouldn't live inside a single tool. Pair Claude Code with Obsidian to build a portable, self-maintaining knowledge base. Practical setup guide."
tags:
  - "clippings"
---
### How to use them in tandem to organize and maintain a personal knowledge base.

> **Bonus:** *Grab the [Claude Code Essentials pack](https://www.whytryai.com/i/190728578/sunday-bonus-93-three-claude-code-skills-that-auto-customize-themselves-to-your-project) with self-building skills, customizable workflows, and copy-paste use cases.*

Look, I wasn’t gonna get all fanboy about this.

I really wasn’t.

When I first wrote about [Claude Code last month](https://www.whytryai.com/p/claude-code-beginner-guide), I figured it’d be a one-off exploration.

But then something happened that—if I’m honest [1](https://www.whytryai.com/p/claude-code-obsidian#footnote-1-188994605) —rarely happens with most AI tools I try: I started regularly using Claude Code in my daily life.

Like, a lot.

So much so that it’s now my primary driver rather than the usual ChatGPT Plus.

![AI-generated illustration of a man running happily through a sunny field alongside a friendly robot labeled "Claude Code," while an angry robot labeled "ChatGPT" watches from a house in the background.](https://substackcdn.com/image/fetch/$s_!UOQK!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F27c062a3-ba5a-405c-bfe1-1f198695e948_1056x703.png)

Oh, the sweet irony of forcing ChatGPT to create this image.

Because of this, I started wondering whether my current folder setup and the way I feed context to Claude Code are as good as they can be.

That’s how I eventually landed on concepts like [“Personal knowledge base” (PKB)](https://en.wikipedia.org/wiki/Personal_knowledge_base) and apps like [Obsidian](https://obsidian.md/).

Then I asked Claude Code to help me set everything up, and I now have a future-proof foundation for capturing knowledge and managing context.

Let me show you how you can do the same.

If you followed along, you should already know how to:

1. ✅ [Get Claude Code up and running on your computer](https://www.whytryai.com/p/claude-code-beginner-guide)
2. ✅ [Set up and use an IDE, Skills, and MCPs with Claude Code](https://www.whytryai.com/p/claude-code-ide-skills-mcp)
3. ✅ [Identify what Claude Code can help you with (and know how to ask for it)](https://www.whytryai.com/p/what-can-you-do-claude-code)

Today, let’s look at how Claude Code can help you organize *and* maintain your context going forward.

## Wait…doesn’t Claude Code already manage its own context?

It does.

I even said as much [in my last article](https://www.whytryai.com/i/186715200/1-context-is-king-but-dont-overengineer-it):

> “But here’s one of my favorite things about Claude Code: Your entire working folder *is* the context. You don’t have to curate and upload individual files to separate conversations. Every new Claude Code chat has access to this full context by default.”

Out of the box, Claude Code already reads your files, saves stuff in MEMORY.md, and can create and edit multiple CLAUDE.md files to give itself additional context.

But there are a few things I’ve come to believe after digging into Claude Code tutorials and watching half the AI Internet [2](https://www.whytryai.com/p/claude-code-obsidian#footnote-2-188994605) lose its damn mind over [OpenClaw](https://openclaw.ai/):

- **Always-on, personal AI agents are coming**: OpenClaw was a vibe-coded one-man project, with all the risks and rough edges that entailed. But it showed the industry that people are hungry for capable agents that take action proactively and can chat with you from just about anywhere. OpenAI [already snatched Peter Steinberger](https://steipete.me/posts/2026/openclaw) (OpenClaw’s creator), so you best believe we’ll soon see official, polished versions of such agents.
- **“Your brain isn’t a filing cabinet”**: In [one of his many posts](https://michaelcrist.substack.com/i/184955320/david-allen-was-only-half-right) about Claude Code, [Michael Crist](https://open.substack.com/users/4651553-michael-crist?utm_source=mentions) said something I agree with: Our brains are built for having ideas and executing on them. Everything in between is busy admin work: color-coding your Trello boards, optimizing your tags, checking off to-do lists, shuffling tasks between “In progress” and “Done,” and so on. That’s why the concept of a self-maintaining personal knowledge base is increasingly fascinating to me.

Given this, I think it makes perfect sense to start building a standalone, organized context repository, untethered from any specific agent.

That way, whenever a new awesome agent comes along—OpenClaw 2.0, Claude Code Extra, Gemini Remote, whatever—I’ll have something I can point at and say, “Here, look, this is me and everything I’m working with. Let’s go!”

![AI-generated illustration of a man laughing at a laptop surrounded by three friendly robots labeled "OpenClaw 2.0," "Claude Code Extra," and "Gemini Remote," while a sulking ChatGPT robot sits alone at a bar in the background.](https://substackcdn.com/image/fetch/$s_!QmyO!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff87d0c00-ed25-408d-9aed-24995384fae4_1402x933.png)

It’s not you, ChatGPT. It’s me.

And that’s exactly where dedicated note-taking and [personal knowledge management (PKM)](https://en.wikipedia.org/wiki/Personal_knowledge_management) apps can come in handy.

They supplement Claude Code’s “blind spots” quite nicely, because they are:

1. **Agent-agnostic:** Your knowledge is not locked into a specific AI tool and can be organized in a way that’s easy for any future agent to parse and work with.
2. **Interconnected:** Instead of fragmented subfolders and files, PKM apps create deep connections between different “objects” (people, places, etc.) spanning across multiple notes. Over time, this web of knowledge grows and becomes more meaningful.
3. **Visual:** Unlike Claude Code’s chat interface, you can surface PKM connections in a visual dashboard, giving you an at-a-glance view of how everything relates. Sort of like a map of your mind. A mind map, if you will. I should trademark that term.
4. **Accessible on the go:** PKM tools typically have dedicated mobile apps that also let you jot down quick thoughts wherever you are and sync directly to your database.

And that, kids, is why I decided to plunge myself straight off a cliff and into the PKM rabbithole. (That sentence sounded way better in my head.)

## But why Obsidian, specifically?

I’ll be upfront: This isn’t the first time I’ve come across Obsidian.

Many people who work with code and knowledge organization swear by it.

So a while back, after hearing yet another recommendation, I gave it a try.

Here’s archive footage of how that went:

<video src="blob:https://www.whytryai.com/49140f92-9e3b-45eb-b716-aa793c982bcd"></video>

Don’t get me wrong.

Obsidian looked light, powerful, and flexible. I could see that, given time, you could build out a super comprehensive database of everything you ever needed.

It’s just that the process of creating all those notes and interconnections was exactly the kind of extra admin work I wanted to avoid.

But that’s exactly the point of this post: Obsidian isn’t for me.

It’s for Claude Code.

And as a tool for Claude to use, Obsidian is near-perfect:

First, Obsidian notes live in a local folder (or “ [vault](https://help.obsidian.md/vault) ”) on your computer. Place that folder inside your working folder, and Claude gets instant access to everything.

Second, Obsidian notes are Markdown files (.md). And guess what? That’s exactly what LLMs like Claude already prefer and use. Claude Code knows how to create, edit, and structure these.

Finally, Obsidian uses \[\[Wikipedia\]\]-style links to connect concepts across your notes, which are also trivial for Claude Code to work with.

It certainly doesn’t hurt that Obsidian is free, either.

That’s why I settled on Obsidian, but you might want to check out these alternatives:

- [Capacities](https://capacities.io/) (cloud-based competitor with a somewhat sexier UI)
- [Logseq](https://logseq.com/) (closest to Obsidian, works with local files, free and open-source)
- [Notion](https://www.notion.com/) (requires quite a bit more legwork to hook up to Claude Code)