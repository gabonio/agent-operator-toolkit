# Domain Organization and Developer Navigation

Load for new applications, new business-capability modules, or approved changes to ownership boundaries. Preserve existing repository conventions and approved architecture in brownfield work; do not reorganize a system to satisfy a generic diagram.

## Design for the next maintainer

- Organize new applications around cohesive business capabilities/features using the product's vocabulary. A developer should find a capability's entrypoint, rules, data contracts, and focused tests without searching unrelated technical layers.
- Make module ownership and allowed dependencies explicit. Keep rules at one owning boundary; consumers use that contract rather than reaching into another module's storage or internals. Extract shared code only after a real shared responsibility emerges.
- Keep business decisions readable with explicit inputs/results and minimal side effects. Isolate database, network, filesystem, and UI effects behind clear adapters where that improves testability; use simple functions/modules when interfaces would add no value.
- Trace one representative user action through entrypoint, business rule, adapter, and result/error. Naming and control/data flow should explain that path without hidden hooks, mutable global state, or clever indirection.
- Scale structure to complexity: a small app may need only a few feature modules in one process. Domain-driven organization does not require microservices, tactical DDD classes, event sourcing, generic repositories, or many layers.

## Acceptance and handoff

Record relevant ownership/dependency decisions in the existing specification or ADR, not a parallel handbook. Include focused tests of business rules and changed adapter contracts; use existing import/build checks for boundaries where available, otherwise review actual dependencies.

When useful, update an existing README/developer guide with a concise developer map: capability-to-path mapping, application entrypoints, setup/run/focused-test commands, and links to key decisions. Create a small onboarding section only when no existing home fits; do not duplicate the map across instruction files. For tiny changes, link existing navigation instead.

Before handoff, locate a representative rule and its test using that map and check the documented run/test path. Report paths, evidence, deferred work, and gaps; a generated directory tree or an agent's quality claim is not proof of maintainability.
