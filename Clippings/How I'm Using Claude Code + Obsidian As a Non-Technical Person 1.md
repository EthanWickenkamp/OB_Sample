---
title: "How I'm Using Claude Code + Obsidian As a Non-Technical Person"
source: "https://www.reddit.com/r/ClaudeAI/comments/1r45eeu/how_im_using_claude_code_obsidian_as_a/"
author:
  - "[[chasing_next]]"
published: 2026-02-13
created: 2026-03-13
description:
tags:
  - "clippings"
---
I've been seeing big gains from the Claude Code + Obsidian combo.

Here's a breakdown of what has been working for me:  
*(see more details about each component* [*here*](https://www.chasingnext.com/how-to-build-a-compounding-ai-operating-system-as-a-non-technical-person/)*).*

**Foundation:**

All of the below tactics rely on these three things.

**1\. My File System**

- Dedicated folder on my computer that I've been building out. All notes, context documents, research, infra, and processes (basically anything I work on these days) go neatly organized here.

**2\. Claude Code**

- Makes the file system powerful with its abiliity to read, write, connect to tools, and execute processes. I paid for the $20/month plan, but quickly jumped to $100.

**3\. Obsidian**

- Lots of complex definitions of what this is, but it's an easy way to see and edit the documents I co-work on with AI. Easy to use and free, can pay $4/month if you want remote access. Love that it autosaves doc edits.

**Tactics That Make My System Compound:**

Here's what I'm doing on top of the foundation to make the system compound.

**1\. System Instructions (Claude.md)**

- The file Claude Code reads at the start of each session telling it the basics. Important to give it just enough info without overloading (it'll burn tokens and get confused). I use it to teach Claude what it should do, what capabilities it has, and where to find deeper info.

**2\. Context Files**

- Markdown documents that hold key info (preferably in JSON format). I have business, ICP, goals, project context in mind. Typically have AI help me draft them by using a browser to scan my website, having it ask me questions, or synthesizing sources.

**3\. Session Recaps**

- Have Claude set up a /handover command that you execute before you close every conversation. This is a way to add "memory" to your system by summarizing and saving what you worked on in files that are available to inform future sessions and queries.

**4\. Search**

- I use QMD developed by the Shopify CEO. Its a local search engine that indexes my files and embeds/ranks your content. An efficient way to find and interact with your files without burning tokens or time. I can ask things like "What language do customers use to describe their AI problems?" and it will provide details and rank results in a way that a standard LLM would struggle with.

**5\. System-Level Workflows (Commands)**

- These are how I run routine processes on my file system. thinks like the /handover command mentioned above, plus /weekly-review and /format-notes. I have AI help create commands when a process is straightforward and I don't need to go back and forth with AI to provide more details or approvals.

**6\. Reusable Workflows (Skills)**

- A step beyond commands. They are the core of my everyday processes. You can add examples, decision logic, multi-step instructions and inject your POV in a way you can't with commands. I have AI help build these by asking it to help build a skill then describing the process I want and having it ask me questions.

**7\. Connect to Tools (APIs & MCPs)**

- APIs and MCPs give my system access to tools and info that Claude can't execute itself. Things like sourcing info, reading/updating data, and completing actions in third-party tools. Most tools today have APIs/MCPs available, but you'll likely have to pay a small fee per use. In my opinion worth it to avoid manual work. AI will help you set them up.

**8\. Organization**

- For this to work well, I need my file system to stay organized. That means having specific folder structure, cleaning up stuff that is misplaced and making things easy for you and AI to locate. I include clear organization in Claude.md for AI to follow.

**9\. Ruthless Auditing**

- Similar to organization, I make sure to get rid of old info since it can kill outputs. Move files I dont use to archive folders, update skills and commands to meet changing needs, regularly review Claude.md and context files so they're up to date.

**10\. Backup & Remote Access (GitHub)**

- This one can sound scarier than it is. GitHub is where my file system lives remotely. It's free cloud storage that tracks changes each time I update it. This way I have backups incase things go wrong and I can use Claude Code on mobile and browser apps.

**11\. Combine Routine Processes**

- Everything I've said so far would be a lot to manage individually. My trick is liking everything I want to maintain into one /weekly-update command. I run this at the end of each week when I need my next week's to-do list. It also archives old docs, updates QMD and my skill inventory log, gives me a weekly review and updates GitHub.

**12\. Not Over-Architecting**

- I've learned this one the hard way... it's easy to get excited and overbuild skills, commands, and custom dashboards for everything. My goal is to build things that will bring more value than the time it takes to create (and occasionally for the sake of experimentation). Even with AI, I find things always take more time than I plan.

That's my current system. Anything I'm missing out on?

Hope this helps someone else get more out of AI. As mentioned above, I broke down each of the above in more details on my site here: [https://www.chasingnext.com/how-to-build-a-compounding-ai-operating-system-as-a-non-technical-person/](https://www.chasingnext.com/how-to-build-a-compounding-ai-operating-system-as-a-non-technical-person/)

---

## Comments

> **ClaudeAI-mod-bot** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o59a0mq/) · 1 points
> 
> **If this post is showcasing a project you built with Claude, please change the post flair to Built with Claude so that it can be easily found by others.**

> **entity\_response** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o59gbjt/) · 47 points
> 
> You’ve explained a lot of components, but I don’t understand what gains you’ve had, or even what you are actually doing with this. It’s hard to tell if it’s useful or not, sorry 
> 
> > **FlatulistMaster** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5br3ep/) · 3 points
> > 
> > I have a similar system and I'll chime in and say that in my line of work, this has helped with processing research and planning documents, returning to them later, making sure related notes get noticed as such and I definitely feel like all of this keeps me better focused on whatever task I have at hand that week.
> > 
> > My work is quite scattered and I have to have an overview of a lot of things, while being able to switch focus many times per month. The system also makes it a lot quicker to prepare for meetings and to save notes from them.
> > 
> > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o59on2h/) · \-7 points
> > 
> > Ah I can see how that didn't come across - essentially, I'm running my everyday work through this file system. Notes, meeting transcripts, project work, to do lists - everything gets saved in here. I'm then using the tactics to build on top of my core info, with elements that do more of the strategic work (analyze, synthesizing, and connecting context) and others that do the manual stuff (formatting, organizing, logging, updating).
> > 
> > The gains come from all the context it has + the fact that AI knows where to find info it needs (much of that due to linking the different tactics together) - which is getting me way better results and suggestions than what I'd used in the past (projects, platform memory, gpts, etc.)
> > 
> > > **Nonomomomo2** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5arcxx/) · 17 points
> > > 
> > > So for example…. Can you name one concrete thing this has helped you with?
> > > 
> > > > **under\_arm\_charm** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5beepd/) · 4 points
> > > > 
> > > > I have a very similar system to this. One simple and helpful thing it does is takes raw granola transcripts and processes them into structured JSON with a yaml style beginning that summarieses the meeting, related it to a project, tiages it into the 'knowledge' fold of that project and interviews me about who was in the meeting (now it knows who's there bases on existing knowledge accurate >90% without asking).
> > > > 
> > > > I make short form documentaries about complex processes in the public sector so I have tonnes of meeting about all sorts of things then have to write scripts that tell an accurate story that juggles info from meetings, interviews, dense documents, just way too much for someone who's not proficient in the subject matter yet (it's a very new gig).
> > > > 
> > > > This one transcript processer skill coupled with project organisation has been a game changer when distilling info down into a narrative script that engaging, accurate and entertaining
> > > > 
> > > > > **under\_arm\_charm** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5beqru/) · 3 points
> > > > > 
> > > > > Also great for building relationships quickly as it helps you remember everything everyone has ever said to you so you can build profiles and role play ideas and building knowledge space for the politics and culture of an org. For some places a total waste but other it's useful
> > > > > 
> > > > > **Nonomomomo2** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bh5d2/) · 2 points
> > > > > 
> > > > > That’s a super useful example thanks!
> > > > > 
> > > > > **leopard-licker** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cdlg8/) · 1 points
> > > > > 
> > > > > What are you using to capture transcriptions?
> > > > > 
> > > > > > **under\_arm\_charm** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cgn2f/) · 1 points
> > > > > > 
> > > > > > Granola - it's a gamechanger
> > > > > > 
> > > > > > > **Fit\_Author3757** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cqsdl/) · 1 points
> > > > > > > 
> > > > > > > Saving this for later
> > > > > > > 
> > > > > > > **leopard-licker** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5d6oyf/) · 1 points
> > > > > > > 
> > > > > > > Thanks I’ll check it out!
> > > 
> > > > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cmghj/) · 2 points
> > > > 
> > > > For one, my current focus is customer research. I’m recording discovery calls with tactiq and saving transcripts (priority in my [Claude.md](http://claude.md/) file). I have specific problems and an ICP I am looking to validate/invalidate (identified through deep research). After each call I run a command that takes the transcript summarizes and pulls out specific info, and also analyzes it relative to my problem and ICP hypothesis. I can interact with individual convos but it also pulls in similar relevant inputs from other convos. I also run the /handover command after each chat which makes it automatically pull in relevant info as I work through other tasks. I can also easily search convos with QMD. I am also pulling out themes, content ideas, and created an interactive dashboard to view details, use as a companion for questions, and real-time notes to keep me focused. I simply could not do the same level of synthesis AI can, and also would be injecting my own biases into analysis if I were doing this manually. This also feeds into other tasks I work on since everything is connected...
> > > > 
> > > > > **Nonomomomo2** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5ctcqk/) · 1 points
> > > > > 
> > > > > Great example thank you! I have a better picture why it’s worth doing the legwork for something like this now. Thanks for taking the time 🙏🏽
> > > 
> > > > **DistributionRight222** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bfee4/) · \-2 points
> > > > 
> > > > She literally named several 😂
> > > > 
> > > > > **Nonomomomo2** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bh8s0/) · 2 points
> > > > > 
> > > > > Such as? I see lots of process, but no product.
> > 
> > > **DenizOkcu** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5atujk/) · 2 points
> > > 
> > > If you want to try taking a step back from the complexity, you could check out an obsidian plugin that I am maintaining: ChatGPT MD (The name is from the old days when it only supported ChatGPT)
> > > 
> > > You can chat with the Claude models from inside your notes ( via Anthropic API). You can link notes for context. You can turn on tool calling in the settings to let the LLM use file search and websearch (via Brave Websearch api). You can create AI personas for different tasks. Let me know what you think.
> > > 
> > > > **DistributionRight222** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bev2y/) · 1 points
> > > > 
> > > > This is also something I will definitely look into. I am not wanting to vibe code my way through my development without actually learning about coding and the rest even if Claude will write most of it doing things the correct way and learning something can only be beneficial thanks for sharing I’ll definitely let you know how it’s going
> > 
> > > **DistributionRight222** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5be0b9/) · 2 points
> > > 
> > > The Same problem I was having Claude suggested obsidian to me way back at the start I’ve been doing a lot of reading researching and you don’t have time to remember everything especially after a long ghost session notes get scattered lost saved on divert drives or not saved at all. That’s counter productive and I originally didn’t like obsidian but just because i didn’t understand it and have now been trying it out again and loving it I will definitely try your suggestions thanks
> > > 
> > > **NotJustAnyDNA** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bnyjw/) · 2 points
> > > 
> > > The gain is that Claude now has the full context of whatever is in Obsidian. I use Claude Code in the vault root sometimes, but I typically just run it in the directory of a specific project to limit the context window. Running against the entire vault just wastes tokens. I also use Claude Code with Ollama as the LLM for some projects that do not need advanced reasoning. This is ideal for most projects… I just have a script in the project root that launches Ollama, Run LLM, then open Claude code with environment variables saying use Ollama. I reserve the Claude connections for advanced code/ complex logic writing.
> > > 
> > > **stiverino** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5ak8hg/) · 4 points
> > > 
> > > Sorry but this sounds like anti productivity. I should know. I’ve been there. You don’t need this much I promise you. The prospect of having a cool system sounds nice in theory but chances are you’ll be back to a simple to do list , notes, and a file system in no time.
> > > 
> > > > **ladyhaly** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bj3jn/) · 2 points
> > > > 
> > > > I use a very similar system, just without Obsidian. I use skills and projects and it's helped so much with my work.
> > > > 
> > > > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cn0xl/) · 1 points
> > > > 
> > > > Not for everyone, but it is helping me. I doubt I'll be going back since I took my old manual system and made it less manual and adaptive.
> > 
> > > **PuzzledBag4964** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cn2l8/) · 1 points
> > > 
> > > Really I find it stips and deletes all my content I am constantly wasting time explaining and recovering files

> **noiv** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bj8pt/) · 4 points
> 
> Also fan of CC + Obsidian. I have Obsidian vault on iCloud and CC's plan directory points into vault. When context runs out, important bits get saved in vault and next iteration picks up. Perfect combo.
> 
> > **Glazed\_and\_Infused** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5far15/) · 1 points
> > 
> > Would you expand on exactly what you are doing? All of the plans you make get saved in your obsidian vault? And then do you always point Claude to your vault to read a CAUDE.md file or something?

> **neuronexmachina** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cc7xn/) · 2 points
> 
> Have you considered creating a public GitHub repo with some of the agent skills/commands you're using? I've been looking at setting up something similar.
> 
> > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5d7xqy/) · 2 points
> > 
> > I just put my first skill up on git last week. Thanks for the idea of putting some of these organizational processes up. [https://github.com/rb-mm/skillmaxxer-3000](https://github.com/rb-mm/skillmaxxer-3000)

> **YUL438** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5d7na1/) · 2 points
> 
> cool project here is another similar one i’m using [https://github.com/heyitsnoah/claudesidian](https://github.com/heyitsnoah/claudesidian)
> 
> > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5d8li8/) · 1 points
> > 
> > wow - this looks awesome! cool idea to put the full structure on github for others.

> **time\_traveller\_x** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cmt2h/) · 2 points
> 
> This looks like a procrastination on stereoids

> **prototype\_\_** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5b7hgt/) · 1 points
> 
> I use obsidian for doco. I connect with Claude's filesystem MCP. The obsidian vault lives on onedrive. I think it gives all the benefits. No need for subscriptions.
> 
> > **DistributionRight222** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bfcgs/) · 4 points
> > 
> > I would get off OneDrive for local drive and GitHub and maybe Google cloud. OneDrive screws everything up delete it
> > 
> > > **prototype\_\_** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bhnkr/) · \-1 points
> > > 
> > > I just haven't had that experience. It's happily syncing across 3 machines.
> > > 
> > > **entity\_response** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5c0z05/) · \-1 points
> > > 
> > > One drive is used by thousands of organizations, I use it for very sensitive project. It does not screw everything up unless you hit a very specific bug or admin error

> **LavoP** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bl4px/) · 1 points
> 
> Built a very similar system for myself. The one thing yours has that mine doesn’t is QMD. I’m going to look into adding this

> **quietbat\_** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5br8li/) · 1 points
> 
> QMD is clever. Token-efficient recall beats context window stuffing.
> 
> > **Glazed\_and\_Infused** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5fbwqm/) · 1 points
> > 
> > What is QMD?

> **oilier\_than\_thou** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5efld2/) · 1 points
> 
> Me when i take too much adderall

> **SchwartzReports** · [2026-02-18](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o63jswd/) · 1 points
> 
> Forgive me, you do not sound like a "non-techical person."

> **\[deleted\]** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5bws5n/) · 2 points
> 
> I get that. It does take upfront work, but I've tried to maintain as much as I can through the weekly command I mention above. The folder structure is pretty set, so I'm mostly running my weekly work and building small system modifications as I go (adding on helpful commands or skills tied to a specific work task I'm working on & know will continue to do).
> 
> > **chasing\_next** · [2026-02-14](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5cnvb9/) · 1 points
> > 
> > I get that. It does take upfront work, but I've tried to maintain as much as I can through the weekly command I mention above. The folder structure is pretty set, so I'm mostly running my weekly work and building small system modifications as I go (adding on helpful commands or skills tied to a specific work task I'm working on & know will continue to do).

> **\[deleted\]** · [2026-02-17](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5ybw9h/) · 2 points
> 
> I like how you're thinking. Just signed up, looking forward to seeing what you launch.
> 
> > **chasing\_next** · [2026-02-18](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o5yqrzd/) · 1 points
> > 
> > I like how you're thinking. Just signed up, looking forward to seeing what you launch.
> > 
> > > **vistdev** · [2026-02-18](https://reddit.com/r/ClaudeAI/comments/1r45eeu/comment/o60fvrf/) · 1 points
> > > 
> > > Awesome! Hope I won’t disappoint.