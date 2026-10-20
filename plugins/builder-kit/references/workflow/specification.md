# Specification Workflow

Follow repository conventions. If none exist, propose:

```text
docs/specs/YYYY-MM-DD-<feature>-design.md
docs/plans/YYYY-MM-DD-<feature>-implementation.md
```

The specification owns behavior and decisions; the plan owns ordered execution. Do not duplicate them.

## Conditional stack-selection interview

Use only for an undecided new application or explicitly requested stack reconsideration, not ordinary changes to an established stack. Read existing decisions, manifests, and constraints first; retain them unless the user approves a change. Do not infer technical ability from the product idea.

Ask one question at a time, only about unknowns that affect the decision. Adapt the next question to the previous answer; this is not a mandatory questionnaire. Explain terms once in everyday language: a runtime runs the code, a framework supplies common app building blocks, and hosting is where the app runs for users.

| Decision area | Plain-language prompt, when unknown |
| --- | --- |
| Users and outcome | What should someone be able to accomplish with this app? |
| Platform | Will people use it as a website, phone app, desktop app, or another tool? |
| Existing constraints or stack | Is there existing software, a required technology, or a team this needs to fit? |
| Hosting/deployment and runtimes | Where do you expect it to run: an existing hosting account, your own server, an app store/device, or somewhere not yet chosen? |
| Integrations and data | What other services or information must it work with, including anything private or sensitive? |
| Scale and workload | How many people or jobs might use it at once? |
| Budget | What monthly running cost would be comfortable? |
| Operations and maintenance ownership | Who will keep it running and make changes after launch? |

Use separate follow-ups for decision-changing details such as offline/live or long-running work, sensitive data, the maintainer's existing skills, or willingness to manage servers; never bundle multiple unanswered questions in one turn. If the user does not know, explain realistic options and record the remaining assumption rather than repeatedly demanding an answer. Check host/runtime versions, build support, database availability, persistent storage, background-job/time limits, region, and costs only where they constrain the proposed workload. Use current official documentation when available; cite evidence and mark unverified hosting claims explicitly, with a validation step. Do not promise free tiers, runtime support, or deployment compatibility from memory.

Recommend one primary **language + runtime/target + framework (or none) + deployment model**, tied to the discovered needs, hosting limits, and maintenance owner. Separate browser/mobile code, server code, and SQL/database roles when applicable; SQL complements an application stack rather than replacing it. Prefer fewer moving parts over novelty. There is no universal default language.

Give one or two meaningful alternatives only when they could change the outcome, with concrete tradeoffs in hosting fit, ecosystem/integrations, delivery effort, performance, cost, or upkeep. For example, existing PHP hosting or a .NET maintenance team can outweigh the appeal of a new stack; a native mobile target introduces different constraints from a browser application. Do not turn examples into automatic prescriptions.

Record the recommendation, rationale, alternatives considered, constraints, evidence/unverified assumptions, unresolved blockers, and approval status in the specification. Require explicit user approval before committing to the selection or scaffolding; an existing approved specification may supply that approval. Specification/plan approvals may be combined for bounded work, but must name the stack decision. If approval or a material compatibility answer is missing, stop before scaffolding. Do not deploy anything during discovery; deployment requires separate authorization naming the application and environment.

## Approval

- Large/high-risk: approve the specification, then the plan.
- Bounded work may combine both approvals.
- Silence, continued discussion, or document creation is not approval.
- Stop for renewed approval on material drift.

## Required quality

Capture objective, users/context, scope/non-goals, source of truth, behavior/contracts, relevant failures, triggered security/performance/compatibility concerns, verification, open decisions, and delivery profile.

For substantive work, make maintainability reviewable: identify the owning capability/module and vocabulary, relevant dependency boundaries, the path from an entrypoint to its rules/adapters, and focused tests. For new apps or ownership changes, apply [domain organization](../architecture/domain-organization.md). Preserve established conventions otherwise; do not invent layers to fill a template.

For data-bearing work, include volume/growth, request bounds, fields/DTO, processing location, query/index/cache behavior, trust boundary, and tests proving scope.

The plan contains target areas, ordered tasks, dependencies, invariants, tests/commands, stop conditions, and evidence. Include relevant readability/ownership checks and a developer handoff through existing docs: module/entrypoint paths, run/test commands, and key decisions or explicit gaps.
