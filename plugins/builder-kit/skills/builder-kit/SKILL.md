---
name: builder-kit
description: Explicitly invoked development harness for safely planning, building, or changing software with an agent. Use only when the user invokes Builder Kit or asks to use the Builder Kit workflow. Classify tiny fixes versus planned work, load only relevant standards and expert lenses, protect unrelated changes, require approval for non-trivial implementation, and verify the result.
disable-model-invocation: true
---

# Builder Kit

Use this skill as a router. Load only references triggered by the task.

## Start

1. Resolve [profiles](../../references/workflow/profiles.md) and [task classification](../../references/workflow/task-classification.md).
2. Read [Git Safety](../../references/workflow/git-safety.md), then inspect repository instructions, relevant code/tests/docs, branch, and status.
3. Apply [authority and legacy guidance](../../references/workflow/authority-and-legacy.md).
4. State the classification and optional lenses briefly; let the user override them.

For a tiny fix, make the smallest coherent change when implementation is requested, then use [verification](../../references/workflow/verification.md). For planned work, read and follow [the develop-from-spec instructions](../develop-from-spec/SKILL.md) and stop at its approval gate.

## Conditional routing

| Trigger                               | Read or invoke                                                                                      |
| ------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Select expert concerns                | [lens routing](../../references/lenses/lens-routing.md), then only selected lens files              |
| Data, APIs, search, lists, caches     | [data boundaries](../../references/architecture/data-boundaries.md)                                 |
| Auth, integrations, external services | [integration boundaries](../../references/architecture/integration-boundaries.md)                   |
| Secrets, permissions, sensitive data  | [security and privacy](../../references/architecture/security-and-privacy.md)                       |
| Frontend styling or components        | [frontend composition](../../references/architecture/frontend-composition.md)                       |
| Mutations, concurrency, migrations    | [reliability and evolution](../../references/architecture/reliability-and-evolution.md)             |
| Language, frontend, SQL, or CI work   | [standards routing](../../references/standards/routing.md), then only matching files                 |
| Specialized platform or service work  | [external capability routing](../../references/workflow/external-capabilities.md), then invoke an available owning skill |
| Prototype project                     | [prototype delivery](../../references/workflow/prototype-delivery.md)                               |
| New application                       | [start-new-app instructions](../start-new-app/SKILL.md)                                       |
| Challenge assumptions or readiness    | [adversarial-review instructions](../adversarial-review/SKILL.md)                             |
| Standard code/design review           | [standard review](../../references/lenses/standard-review.md)                                       |
| Repeated review of current changes    | [PR review loop instructions](../pr-review-loop/SKILL.md)                                     |
| Maintaining or releasing Builder Kit  | [release and update policy](../../references/workflow/release-and-updates.md)                       |

Mandatory safety, security/privacy, accessibility, bounded-data, authorization, and trust-boundary guidance still applies when triggered. Never implement non-trivial work before approval, replace local conventions without cause, or disturb unrelated user work.
