# {{FEATURE_NAME}} — Implementation Plan

**Status:** Draft — awaiting approval
**Specification:** {{SPEC_PATH}}
**Communication profile:** {{COMMUNICATION_PROFILE}}
**Delivery profile:** {{DELIVERY_PROFILE}}
**Delivery strategy:** {{LOCAL_ONLY_OR_INCREMENTAL_DRAFT_PR}}
**Approved GitHub writes:** {{NONE_OR_BOUNDED_DRAFT_PR_PUSH_AND_REVIEW_SCOPE}}

Implement only after approval. The specification owns behavior; this plan owns order. Follow repository rules, preserve unrelated work, and stop on material drift.

## Invariants and non-goals

- {{INVARIANT}}
- Non-goal: {{NON_GOAL}}

## Delivery order

1. {{DEPENDENCY_OR_PROVIDER_FIRST_STEP}}

## Tasks

### Task 1: {{TASK_NAME}}

Target: {{TARGET}}

- [ ] {{LITERAL_IMPLEMENTATION_STEP}}
- [ ] {{CONTRACT_OR_STATE_REQUIREMENT}}
- [ ] {{FOCUSED_TEST}}

Evidence/checkpoint: {{COMMAND_RESULT_AND_REVIEWED_HEAD_IF_APPLICABLE}}

Delivery checkpoint:

- [ ] Slice verification passes.
- [ ] Authorized commit and push to the draft PR are complete when applicable.
- [ ] Incremental review is clean at {{REVIEWED_HEAD}} before the next slice begins.

## Verification and completion

- [ ] Focused tests for changed behavior.
- [ ] Applicable type/lint/static checks.
- [ ] Closest feasible local production-like build.
- [ ] Cross-slice behavior and interactions verified.
- [ ] Relevant capability ownership/dependencies and readable entrypoint-to-rule/test flow reviewed against the approved architecture.
- [ ] Useful developer navigation, run/test path, and key decisions linked or updated in existing docs; handoff gaps recorded.
- [ ] Relevant entry-path/rendered-state smoke test.
- [ ] Final whole-PR review completed when authorized.
- [ ] Diff/status confirms only intended work.
- [ ] Evidence and residual risks reported.

## Stop conditions

- Material plan drift.
- Unsafe overlap with unrelated changes.
- Missing user/product/security decision.
- Required verification cannot be completed safely.
