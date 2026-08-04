# Jenkins and CI Standards

Keep one job/use case responsible for four separable concerns:

1. generation: DSL/seed definitions and parameters;
2. orchestration: stages, errors, logs, and artifacts;
3. dependency gathering: tools, versions, environment, files;
4. payload: low-level testable scripts that perform the work.

Team defaults:

- Make parameters explicit and follow local Groovy/Python style.
- Validate node/platform/tool/file preconditions before executing payloads.
- Pass payload configuration through explicit arguments; avoid hidden environment/path inference.
- Prefer clear stages over deeply nested job hierarchies.
- Minimize plugin dependencies and justify each addition.
- Log enough command context to diagnose failures without exposing secrets.
- Unit-test payloads/helpers and mock CI steps; validate pipeline syntax with repository tooling.
- Preserve existing release, credential, agent-label, artifact, and notification conventions unless the approved change targets them.
