# Expert Lens Routing

Lenses expose questions; they are not personas or independent evidence. Propose at most two primary lenses plus the adversarial review lens unless the work is genuinely cross-cutting. The user may add/remove optional lenses.

| Trigger                                          | Read                                                        |
| ------------------------------------------------ | ----------------------------------------------------------- |
| value, scope, workflow, acceptance               | [product and requirements](product-and-requirements.md)     |
| usability, flow, visual hierarchy, design intent | [UX and UI design](ux-and-ui-design.md)                     |
| browser, components, client state                | [frontend engineering](frontend-engineering.md)             |
| API, service, server behavior                    | [backend engineering](backend-engineering.md)               |
| schema, queries, growth, analytics               | [data engineering](data-engineering.md)                     |
| cross-service boundaries or large blast radius   | [systems architecture](systems-architecture.md)             |
| tests, regression, release evidence              | [quality engineering](quality-engineering.md)               |
| observability, resilience, capacity, deployment  | [reliability and operations](reliability-and-operations.md) |
| compliance with approved design and local rules  | [standard review](standard-review.md)                       |
| pressure-test assumptions/readiness              | [adversarial review](adversarial-review.md)                 |

Security/privacy, accessibility, data sustainability, destructive safety, authorization, and trust boundaries are mandatory guardrails when triggered, not optional lenses.

Convert useful findings into explicit objectives, context, constraints, success criteria, evidence, non-goals/permissions, verification, and stop conditions. Record applied lenses for traceability, but give the executor the decisions—not “act as…” instructions.
