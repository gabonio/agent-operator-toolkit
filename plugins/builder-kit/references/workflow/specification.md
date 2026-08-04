# Specification Workflow

Follow repository conventions. If none exist, propose:

```text
docs/specs/YYYY-MM-DD-<feature>-design.md
docs/plans/YYYY-MM-DD-<feature>-implementation.md
```

The specification owns behavior, decisions, and acceptance criteria. The plan owns ordered execution. Do not repeat whole sections.

## Approval

- Large/high-risk: approve specification, then create and approve the plan.
- Bounded feature: specification and plan may receive combined approval.
- Silence, continued discussion, or document creation is not approval.
- Stop for renewed approval on material drift.

## Required quality

State objective, users/context, scope/non-goals, source of truth, relevant states and failures, contracts, security/privacy, performance/sustainability, compatibility/migration, verification, rollout/rollback when relevant, open decisions, applied lenses, and delivery profile.

For data-bearing work specify current/future volume, query/request scope, pagination/limit, fields transferred, DTO/contract, processing location, indexes/query behavior, cache bounds/staleness, trust boundary, and tests proving request scope.

The implementation plan is the executor packet. It contains checkboxes, target files/areas, dependencies/order, invariants, concrete tests/commands, stop conditions, and evidence fields. It must not rely on persona prompts or architectural inference.
