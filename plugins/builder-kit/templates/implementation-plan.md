# {{FEATURE_NAME}} — Implementation Plan

**Status:** Draft — awaiting approval
**Specification:** {{SPEC_PATH}}
**Communication profile:** {{COMMUNICATION_PROFILE}}
**Delivery profile:** {{DELIVERY_PROFILE}}
**Applied lenses:** {{APPLIED_LENSES}}

## Executor instructions

- Implement only after explicit approval.
- Treat the specification as the behavioral/architectural source and this plan as the ordered handoff.
- Follow repository instructions and preserve unrelated work.
- Do not substitute persona prompts for the concrete decisions below.
- Stop for renewed approval on material scope, behavior, contract, dependency, security, migration, or deployment drift.
- Check off tasks and record concise evidence.

## Invariants and non-goals

- {{INVARIANT}}
- Non-goal: {{NON_GOAL}}

## Dependencies and delivery order

1. {{DEPENDENCY_OR_PROVIDER_FIRST_STEP}}

## Tasks

### Task 1: {{TASK_NAME}}

Target files/areas:

- {{TARGET}}

- [ ] {{LITERAL_IMPLEMENTATION_STEP}}
- [ ] {{CONTRACT_OR_STATE_REQUIREMENT}}
- [ ] {{FOCUSED_TEST}}

Evidence:

- {{COMMAND_AND_RESULT}}

## Verification and completion

- [ ] Focused tests for changed behavior.
- [ ] Applicable type/lint/static checks.
- [ ] Closest feasible local production-like build.
- [ ] Real entry-path or rendered-state smoke test when relevant.
- [ ] Diff/status confirms only intended work.
- [ ] Exact evidence and residual risks reported.

## Stop conditions

- Material plan drift.
- Unsafe overlap with unrelated changes.
- Missing user/product/security decision.
- Required verification cannot be completed safely.
