# Expert Lens Routing

Lenses expose questions, not personas or independent evidence. Load at most two primary lenses unless the work is genuinely cross-cutting; the user may override them.

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

Security/privacy, accessibility, bounded data, destructive safety, authorization, and trust boundaries remain mandatory when triggered. Give the executor resulting decisions, not lens or persona prompts.
