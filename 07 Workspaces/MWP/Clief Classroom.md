
[Jake Van Clief - YouTube](https://www.youtube.com/@JEVanClief)


## Intro to Claude Code



### Session 1

Don't use it like a search engine, copy and pasting it

Problem to solve is the interface of what it can reach how it delivers it

Hes using claude code in vscode, basic implementation

Im using claude code in obsidian dir but terminal, nice frontend for md files, extra commands and rest api

Same model: 
1. desktop - chat interface
2. vscode - editor layer
3. terminal - command line layer
methods of interacting with it

Cursor, Windsurf, Copilot different products with different models on top of vscode

#### Setup
install node.js, i like nvm

can install claude code from npm package manager
`npm install -g @anthropic-ai/claude-code`

type
`claude` to launch terminal

login with pro/max account or api, 

#### Agentic Coding tools
All built around vscode at the core level





### Folder Architecture



## Learning the Abstraction


### 1 Line Python; 12,000 Lines of Code

#### Layer 1: Python


#### Layer 2: Abstract Syntax Tree
Parses code into a tree structure
![[JVC-260312-11.png]]


#### Layer 3: Bytecode
Each instruction is a simple, atomic operation


#### Layer 4: The C Interpreter

#### Layer 5: Assembly
Operations on registers

#### Layer 6: Machine


#### Layer 7: Hardware

#### Layer 8: Transistors

#### Layer 9: Quantum


### Clawdbot, Just Pipelines

Gives you hands everywhere, give it access to anything
Open source, share pipelines and modify for use

#### Orchestration
It is orchestration of AI, there is no AI in it

Message -> AI -> Tools -> Channels -> Back to User

A central router, adding defined outcomes and hooks

#### Modules

##### Channels
**35%** of code
WhatsApp, Telegram, Discord, Signal
Maintained open source libraries that work with these platforms

##### Gateway
**25%** of code
inputs, authentication
Web socket server
routing messages and sessions

##### AI models
**0%**
intelligence, inference compute, send prompts+context
You have to give it api endpoint

##### Tools
**20%** of code
Some built in
browser, bash shell, file system, cron, 
Webhooks
Node tools

##### Persistant Storage
?
##### CLI
**10%** of code
Configuration, api calls

#### 60/30/10 Framework
60% traditional code
30% routing logic
10% AI LLM API calls configured

The value is in whats around the ai, not the ai itself
The infrastructure or scaffolding

#### The good parts
Model agnostic
Self host private data
Open Source, share features
The Infrastructure is your product


