# Operations

Deploy scripts, monitoring configuration, and operational runbooks.

## Infrastructure

- Hosting: [Platform and tier]
- Database: [Managed/self-hosted, provider, backup schedule]
- CDN: [If applicable]
- Domain: [Domain and DNS provider]

## Deploy process

[Step by step: how code goes from merged PR to production.
Include any manual steps, approval gates, or staging environments.]

## Monitoring

- [What is monitored: uptime, errors, performance, etc.]
- [Where alerts go: email, Slack, PagerDuty, etc.]
- [What triggers an alert vs what is logged quietly]

## Runbooks

Store runbooks in /scripts/ for common operational tasks:
- How to rollback a deploy
- How to reset a stuck job
- How to restore from backup
- How to investigate a performance issue

## Rules

- Do not deploy on Fridays. [Or whatever your deploy rules are.]
- All deploy scripts must be idempotent (safe to run twice).
- [Any other operational rules]
