---
name: develop-from-spec
description: Specification-driven workflow for non-trivial software changes. Use when the user explicitly invokes this skill, Builder Kit routes planned work here, or the user asks to discover, specify, plan, approve, implement, and verify a substantial feature. Enforce approval before implementation and use the plan as the executor handoff.
---

# Develop from Spec

## Workflow

1. **Discover.** Read local instructions, relevant architecture/design documents, neighboring code and tests, build/delivery rules, and sources of truth. Load only matching references and lenses.
2. **Specify.** Follow the repository's document convention. If none exists, propose `docs/specs/YYYY-MM-DD-<feature>-design.md`. Use [the specification workflow](../../references/workflow/specification.md) and [the template](../../templates/specification.md).
3. **Approve the specification.** For large or high-risk work, stop for this approval before writing the implementation plan.
4. **Plan.** Follow the repository convention or propose `docs/plans/YYYY-MM-DD-<feature>-implementation.md`. Use [the plan template](../../templates/implementation-plan.md). Make it literal enough for a faster executor without duplicating the specification.
5. **Approve the plan.** Stop before implementation until the user unambiguously approves. Bounded features may receive combined specification-and-plan approval.
6. **Execute.** Follow ordered checkboxes, preserve unrelated work, make the smallest approved change, and record evidence. Ask for renewed approval on material drift.
7. **Verify.** Run focused checks while iterating and the closest local production-like build before PR readiness. Report exact evidence and unresolved risk.

## Material drift

Stop for renewed approval before changing scope, acceptance criteria, architecture, public behavior, data/API contracts, dependencies, security or authorization boundaries, migrations, or deployment behavior. Small implementation details may change when they preserve the approved design; record meaningful deviations.

## Executor handoff

The implementation plan is the handoff. Do not create a third summary. The executor follows concrete decisions, contracts, constraints, tests, stop conditions, and commands—not persona prompts or lens names. Recommend planning and execution capabilities using [model profiles](../../references/model-profiles.md), not a permanently pinned model name.
