# {{FEATURE_NAME}} — Design Specification

**Status:** Draft — awaiting approval
**Date:** {{DATE}}
**Communication profile:** {{COMMUNICATION_PROFILE}}
**Delivery profile:** {{DELIVERY_PROFILE}}

## Objective

{{USER_VISIBLE_OUTCOME_AND_CONTEXT}}

## Success criteria

- {{MEASURABLE_OR_OBSERVABLE_SUCCESS}}

## Scope

### In scope

- {{IN_SCOPE}}

### Non-goals

- {{NON_GOAL}}

## Current system

{{CURRENT_BEHAVIOR_OWNERSHIP_AND_EVIDENCE}}

## Decisions and contracts

{{COMPONENTS_DATA_FLOW_CONTRACTS_AND_DECISIONS}}

For substantive changes, name the owning business capability and vocabulary, relevant module dependencies, and the entrypoint/rule/adapter/test paths. Preserve approved local architecture; omit inapplicable structure rather than inventing layers.

{{CAPABILITY_OWNERSHIP_AND_NAVIGATION_OR_EXISTING_DESIGN_LINK}}

### Stack selection (only when choosing or reconsidering a stack)

Omit this subsection for work that preserves an established stack.

- Primary language, runtime/target, framework (or none), and deployment model: {{PROPOSED_STACK}}
- Fit to users/platform, existing constraints, integrations/data, scale, budget/operations, and maintenance owner: {{RATIONALE}}
- Meaningful alternatives and tradeoffs: {{ALTERNATIVES_OR_NOT_APPLICABLE}}
- Hosting/runtime evidence and unverified assumptions with validation steps: {{EVIDENCE_AND_GAPS}}
- Blocking decisions and explicit user approval status: {{BLOCKERS_AND_STACK_APPROVAL}}

## States and failures

{{RELEVANT_LOADING_EMPTY_PARTIAL_STALE_ERROR_PERMISSION_OR_RETRY_STATES}}

## Triggered concerns

Include only relevant data/performance, security/privacy, compatibility/migration, rollout/rollback, or prototype decisions.

- {{TRIGGERED_DECISION_OR_NOT_APPLICABLE}}

## Verification strategy

{{TESTS_BUILDS_ENTRY_PATH_AND_RUNTIME_EVIDENCE}}

## Open decisions and risks

- {{OPEN_DECISION_OR_RISK}}

## Approval

Approval does not authorize material drift, publication, or deployment unless separately stated.
When selecting a stack, approval must explicitly cover that selection before scaffolding.
