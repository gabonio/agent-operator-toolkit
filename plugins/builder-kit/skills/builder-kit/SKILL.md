---
name: builder-kit
description: Explicitly invoked development harness for safely planning, building, or changing software with an agent. Use only when the user invokes Builder Kit or asks to use the Builder Kit workflow. Classify tiny fixes versus planned work, load only relevant standards and expert lenses, protect unrelated changes, require approval for non-trivial implementation, and verify the result.
---

# Builder Kit

Use this skill as a thin router. Do not load every reference.

## Start

1. Read [profiles](../../references/workflow/profiles.md) and resolve the communication and delivery profiles.
2. Read [task classification](../../references/workflow/task-classification.md).
3. Inspect repository instructions, neighboring code, tests, build files, documentation, branch, and uncommitted changes.
4. Explain the classification and proposed lens set in language appropriate to the communication profile. Let the user override optional lenses and classification.
5. Apply the authority order in [authority and legacy guidance](../../references/workflow/authority-and-legacy.md).

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
| Java, frontend, Python, C++, Jenkins  | Only the matching file under `../../references/standards/`                                          |
| Specialized platform or service work | [external capability routing](../../references/workflow/external-capabilities.md), then invoke an available owning skill |
| Prototype project                     | [prototype delivery](../../references/workflow/prototype-delivery.md)                               |
| New application                       | [start-new-app instructions](../start-new-app/SKILL.md)                                             |
| Challenge assumptions or readiness    | [adversarial-review instructions](../adversarial-review/SKILL.md)                                   |
| Standard code/design review           | [standard review](../../references/lenses/standard-review.md)                                       |
| Repeated review of current changes    | [PR review loop instructions](../pr-review-loop/SKILL.md)                                           |
| Maintaining or releasing Builder Kit  | [release and update policy](../../references/workflow/release-and-updates.md)                       |

Mandatory safety, security/privacy, accessibility, data-sustainability, authorization, and trust-boundary guidance applies when triggered even if the user declines optional lenses.

## Boundaries

- Do not impose Builder Kit when it was not invoked.
- Do not replace local conventions with generic preferences.
- Do not use persona language as a substitute for objective, constraints, success criteria, and verification.
- Do not implement non-trivial work before explicit approval.
- Do not discard, overwrite, stage, or absorb unrelated user work.
