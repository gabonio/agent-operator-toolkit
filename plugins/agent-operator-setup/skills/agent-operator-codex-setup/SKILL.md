---
name: agent-operator-codex-setup
description: Install, update, or diagnose the Agent Operator marketplace in Codex. Use when a user asks to register this marketplace, make its plugins appear, refresh an existing installation, troubleshoot discovery, or verify a local checkout. Prefer native Codex marketplace commands and read-only diagnosis; never replace unrelated personal marketplace or Codex configuration.
---

# Agent Operator Codex Setup

Use native Codex marketplace commands first. Do not manually edit user configuration when the supported command can perform the operation.

## Install

1. Confirm that `git` and `codex` are available.
2. Register the marketplace:

   ```sh
   codex plugin marketplace add git@github.com:gabonio/agent-operator-toolkit.git
   ```

3. Restart Codex if the marketplace does not appear immediately.
4. Open `/plugins`, select **Agent Operator**, and install only the plugins the user wants.
5. Start a new task after installation so it loads the new skill instructions.

## Update

1. Discover the registered marketplace name instead of guessing it.
2. Run `codex plugin marketplace upgrade <marketplace-name>`.
3. Restart Codex or start a new task when cached skill instructions remain active.
4. Run the doctor after an update if discovery or versions still look wrong.

## Diagnose

From this plugin root, run:

```sh
python3 scripts/doctor.py --client codex
```

Pass `--marketplace-root <path>` when diagnosing a specific checkout. The doctor is read-only.

## Boundaries

- Preserve unrelated marketplaces, plugins, agents, hooks, MCP servers, and Codex configuration.
- Do not add startup hooks or background update behavior without explicit permission.
- Do not claim an update is active in the current task; cached instructions may require a new task.
- Ask before deleting caches, replacing checkouts, or modifying user-scoped files.
