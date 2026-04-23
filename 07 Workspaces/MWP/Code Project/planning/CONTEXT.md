# Planning

Feature specs, architecture documents, and decision records.

## How specs work here

A spec describes WHAT to build and WHY, not HOW to build it.
Claude reads the spec and makes implementation decisions based
on the conventions in /src/CONTEXT.md.

## Spec template

When writing a new spec, follow this structure:

### [Feature Name]

**Problem:** What is the user problem this solves?
**Proposal:** What are we building?
**Scope:** What is included? What is explicitly excluded?
**Dependencies:** What does this touch? What needs to exist first?
**Open questions:** What is not decided yet?

## Architecture

Key architecture documents live in /architecture/.
Reference these when building new features to maintain consistency.

## Decision records

When we make a significant technical decision, record it in /decisions/.
Format: YYYY-MM-DD_decision-title.md

### Decision record template

**Decision:** [What we decided]
**Context:** [Why this came up]
**Options considered:** [What else we looked at]
**Rationale:** [Why we chose this option]
**Consequences:** [What this means going forward]
