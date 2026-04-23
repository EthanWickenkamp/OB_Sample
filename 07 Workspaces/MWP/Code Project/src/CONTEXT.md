# Source Code

The application codebase.

## Structure

src/
├── components/    — [UI components]
├── services/      — [Business logic, API calls]
├── utils/         — [Shared utilities and helpers]
├── db/            — [Database queries and migrations]
├── api/           — [Route handlers / endpoints]
├── middleware/     — [Auth, logging, error handling]
├── types/         — [TypeScript types and interfaces]
└── tests/         — [Test utilities and fixtures]

## Patterns we follow

- [State management approach]
- [Error handling approach]
- [Logging approach]
- [How API responses are structured]
- [How database queries are organized]

## Patterns we avoid

- [List specific anti-patterns with brief reasons]

## Testing requirements

- [Minimum coverage expectations]
- [What must have tests (API routes, business logic, etc.)]
- [What does not need tests (pure UI layout, config files, etc.)]
- [How to write a test: framework, assertion style, mock approach]

## Environment

- Required env vars are listed in .env.example
- Do not hardcode values that should be environment variables
- [Any other environment-specific notes]
