---
name: develop-from-spec
description: Specification-driven workflow for non-trivial software changes. Use when the user explicitly invokes this skill, Builder Kit routes planned work here, or the user asks to discover, specify, plan, approve, implement, and verify a substantial feature. Enforce approval before implementation and use the plan as the executor handoff.
disable-model-invocation: true
---

# Develop from Spec

Read [Git Safety](../../references/workflow/git-safety.md) before editing or publishing.

1. **Discover.** Read local rules, sources of truth, relevant design, code, tests, and delivery constraints. Load only matching references and lenses.
2. **Specify and plan.** Follow [the specification workflow](../../references/workflow/specification.md) and repository conventions; otherwise use the [specification](../../templates/specification.md) and [plan](../../templates/implementation-plan.md) templates. Keep behavior/decisions in the specification and ordered execution in the plan.
3. **Approve.** Large or high-risk work needs specification approval before planning. All non-trivial work needs unambiguous plan approval before implementation; bounded work may combine both approvals.
4. **Execute coherent slices.** Preserve unrelated work, follow the plan, verify each slice, and record concise evidence. An incremental draft-PR sequence requires explicit authorization for the draft PR, bounded pushes, and reviewer invocations; plan approval alone does not authorize publication. Complete each review checkpoint before starting the next slice. Do not split tightly coupled changes merely to shrink a diff.
5. **Verify together.** Run cross-slice checks and the closest feasible production-like build. When authorized, finish with a whole-PR review. Report exact evidence and residual risk.

## Material drift

Stop for renewed approval before changing scope, acceptance criteria, architecture, public behavior, data/API contracts, dependencies, security or authorization boundaries, migrations, or deployment behavior. Small implementation details may change when they preserve the approved design; record meaningful deviations.
