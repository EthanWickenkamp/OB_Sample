---
title: "I put Claude Code inside Obsidian, and it was awesome"
source: "https://www.xda-developers.com/claude-code-inside-obsidian-and-it-was-eye-opening/"
author:
  - "[[Joe Rice-Jones]]"
published: 2026-02-07
created: 2026-04-01
description: "No I don't know what I'm doing, but that's what Claude is for"
tags:
  - "clippings"
---
I'm also a [late convert to Obsidian](https://www.xda-developers.com/i-finally-started-using-obsidian-and-i-regret-waiting-this-long/), not because I don't need to take copious notes for future reference, but because I'm terrible at taking notes and using [productivity apps](https://www.xda-developers.com/productivity-apps-you-need-on-linux/) in general. They're just more executive function noise that I can often do without, until, of course, I forget something important and things go crashing down. But then I started wondering if I could [outsource the note-taking to AI](https://www.xda-developers.com/here-are-some-markdown-tips-and-tricks-to-improve-your-note-taking-in-obsidian/), and gears started whirring in my brain.

You see, Obsidian's Markdown format is perfect for use with LLMs. And the CEO of Obsidian already has a ready-to-go set of Agent Skills for Obsidian that you can install by dropping the files into a folder in your Vault. A few hours later, I had a working model connected together, and a brain full of ideas on what I could make Claude Code create for me. It's transformed how I research, how I connect new concepts to those I've previously covered, and how I keep relevant information and the best part is that it didn't take any coding knowledge or a lot of time to get running.

## Why would you want to put an LLM inside Obsidian?

### Create the memory and context that LLMs lack

![claude code inside obsidian](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/claude-code-obsidian.jpg?q=49&fit=crop&w=825&dpr=2)

Claude Code has turned into an incredible resource for me, especially in research, because Google Search is broken, and I want to see resources and not summaries. I can now outsource my browsing, which is incredible, because I can have the AI agents research my next project while I'm working on the current one. It's like having an intern, and like any responsible manager, I do double-check any results, but that still means plenty of time saving overall.

And thanks to Claude's open standard Agent Skills, it's a perfect pairing to live inside my Vault. Instead of adding AI to the app and decide on which features it can handle, Obsidian decided to outline how to use the underlying files, so that the LLM can learn the context, and the guard-rails, for perfect harmony.

The Obsidian Skills folder defines the three major Obsidian file types, so that AI can create files built to those specifications for use in your Vault:

- **Obsidian's custom Markdown**
- **Obsidian Bases**
- **JSON Canvas**

The best part about this arrangement is that it lets the LLM be the smart one in the room. I could figure out how to create these files from my daily notes, or from the websites that I browse during research, but that takes time that I could be doing other things with. And by integrating the LLM into my knowledge repository, I can define the structure of my notes, and how Claude or any other LLM interacts with them.

### Everything is better with a terminal window

![claude on mac](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/01/claude-on-mac.jpeg?q=49&fit=crop&w=825&dpr=2)

I could have [connected Claude to Obsidian](https://www.xda-developers.com/connected-claude-with-obsidian-and-never-looking-back/), and managed my Vault from the Claude app. Except, I'm a visual worker, and prone to forgetting things if I can't see them in front of me, and the whole point of this setup is so that I don't have to remember things. When I use the Claude app, I find I'm spending time trying to remember what I wanted to ask, and I get annoyed having to point it at Obsidian in every command.

By embedding a Terminal window in Obsidian and bringing Claude Code into that, I can now chat to the LLM while having every folder I use in view, a constant reminder of what I'm doing, the context around it, and also see newly created resources as they appear. That's seconds of time I save during every interaction with Claude, which adds up very quickly over the course of a conversation.

- [Download Obsidian](https://obsidian.md/download)
- [See at Github](https://github.com/polyipseity/obsidian-terminal) [See at Official Site](https://obsidian.md/plugins?id=terminal)
- [See at Github](https://github.com/kepano/obsidian-skills)

## Time to curse my Obsidian notes

### But on a fresh account just in case

![setting up claude code inside obsidian](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/claude-code-obsidian-setup-1.jpg?q=49&fit=crop&w=825&dpr=2)

Obsidian is powerful on its own, but adding community plugins makes it next-level. The first one you need is **Terminal**, which takes a few seconds to install and enable, but to get the Agent Skills takes a little manual work. I'm using Claude Code, so I grabbed the contents of the obsidian-skills GitHub repo and dumped them in a **.claude** folder inside my Obsidian Vault.

![claude code creating folder structure in obsidian vault](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/claude-code-obsidian-setup-folders.jpg?q=49&fit=crop&w=825&dpr=2)

And that's it. Claude Code is now able to access my Obsidian Vault. I can create new Skills in natural language to create Research personas, or other agentic workflows, and then those are a few keystrokes away from the Terminal.

The first thing I got Claude to do was to "Create a minimal Obsidian folder structure for a software developer who takes daily notes and wants a long-term second brain," after seeing this in action on the [Coding with ADHD YouTube channel](https://www.reddit.com/r/ClaudeCode/comments/1qln9zt/how_i_take_daily_notes_in_obsidian_with_claude/). It would have taken me hours to set up this structure, assuming that I progressed past decision paralysis, and Claude did it in seconds.

![init claude code in obsidian for memory storage](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/02/claude-code-obsidian-init.jpg?q=49&fit=crop&w=825&dpr=2)

Now we run **/init** which sets up Claude Code inside Obsidian by adding **CLAUDE.md** to the root of our vault. This markdown file will actually be Claude's memory while we're using it through Obsidian, as it is loaded into every chat session so that the LLM has context and understands the conventions used in this vault.

### Now Claude is in charge of my Obsidian Vault

I've also added the Obsidian Web Clipper to every browser I use, because sometimes that linking is easier than writing out a quick note. Claude can read these saved clips, and create summaries or find connections between the newest thing I'm interested in and the things I was working on the month before, and give me ideas on how to connect the two to make my home lab better, or my Obsidian Vault more organized.

It's an absolute game-changer in the way I work, and the amount of work I can get done, and acts as a first-brain for my long-term memory, which isn't the best at times.

### Claude Code inside Obsidian is the local NotebookLM that I was looking for

I can't say that I'm particularly good at organization, most times I try everything gets dumped in one folder named **To Sort**, which dear reader, does not ever get sorted. I've tried automating this before and found the automation setup to be more work than doing it manually, which didn't fix things at all. But having an LLM inside my knowledge vault means I can make it do all the drudgery that I abhor, and gives me more time to read, assimilate, and put concepts into practice.