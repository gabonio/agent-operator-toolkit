# Specification Workflow

Follow repository conventions. If none exist, propose:

```text
docs/specs/YYYY-MM-DD-<feature>-design.md
docs/plans/YYYY-MM-DD-<feature>-implementation.md
```

The specification owns behavior and decisions; the plan owns ordered execution. Do not duplicate them.

## Approval

- Large/high-risk: approve the specification, then the plan.
- Bounded work may combine both approvals.
- Silence, continued discussion, or document creation is not approval.
- Stop for renewed approval on material drift.

## Required quality

Capture objective, users/context, scope/non-goals, source of truth, behavior/contracts, relevant failures, triggered security/performance/compatibility concerns, verification, open decisions, and delivery profile.

For data-bearing work, include volume/growth, request bounds, fields/DTO, processing location, query/index/cache behavior, trust boundary, and tests proving scope.

The plan contains target areas, ordered tasks, dependencies, invariants, tests/commands, stop conditions, and evidence.
