# [App Name]

[One sentence: what this app does and who uses it.]

## Tech Stack

- Language: [TypeScript, Python, Go, etc.]
- Frontend: [React, Vue, Svelte, none, etc.]
- Backend: [Express, FastAPI, Django, etc.]
- Database: [PostgreSQL, MongoDB, SQLite, etc.]
- Auth: [Method — JWT, OAuth, session, etc.]
- Deploy: [Platform — Vercel, AWS, Railway, etc.]
- CI/CD: [Tool — GitHub Actions, CircleCI, etc.]

## Workspaces

- /planning — Feature specs, architecture docs, decision records
- /src — Application code
- /docs — API documentation, user guides, changelog
- /ops — Deploy scripts, monitoring, operational runbooks

## Routing

| Task | Go to | Read | Skills |
|------|-------|------|--------|
| Spec a feature | /planning | CONTEXT.md | — |
| Write code | /src | CONTEXT.md | testing |
| Write docs | /docs | CONTEXT.md | doc-authoring |
| Deploy or debug | /ops | CONTEXT.md | — |
| Review code | /src | CONTEXT.md + specific files | testing |
| Record a decision | /planning/decisions | CONTEXT.md | — |

## Commands

| Action | Command |
|--------|---------|
| Dev server | [your command] |
| API server | [your command] |
| Run all tests | [your command] |
| Run single test | [your command] |
| Build | [your command] |
| Lint | [your command] |
| DB migrate | [your command] |
| DB seed | [your command] |

## Conventions

- [Component style: functional only, class-based, etc.]
- [File organization: routes in X, queries in Y, utils in Z]
- [Naming: PascalCase for components, camelCase for functions, kebab-case for files, etc.]
- [Testing: tests next to code (feature.test.ts) or in /tests/ mirror]
- [Commits: conventional commits (feat:, fix:, docs:, chore:)]
- [Decision records: /planning/decisions/YYYY-MM-DD_title.md]

## Avoid

- [Libraries to not use and why]
- [Patterns to not follow and why]
- [Files or directories to not modify directly]
- [Anti-patterns specific to your codebase]

## Current State

- [What is working, what is in progress, what is broken]
- [Any active refactors or migrations]
- [Known tech debt and where it lives]
