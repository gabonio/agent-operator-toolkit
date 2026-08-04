# Agent Operator for Codex

Agent Operator is distributed to Codex as a native plugin marketplace.

## Install

Run from a terminal:

```sh
codex plugin marketplace add git@github.com:gabonio/agent-operator-toolkit.git
```

Restart Codex if needed, open `/plugins`, choose **Agent Operator**, and install only the plugins you want:

- `agent-operator-setup` for installation and diagnosis
- `builder-kit` for development and adversarial review workflows
- `marketplace-management` for plugin marketplace maintenance

Start a new task after installation so the new skill instructions are loaded.

## Update

Discover the configured marketplace name, then run:

```sh
codex plugin marketplace upgrade agent-operator-toolkit
```

Restart Codex or begin a new task if the active task still uses older skill instructions.

## Diagnose

From a marketplace checkout:

```sh
python3 plugins/agent-operator-setup/scripts/doctor.py --client codex --marketplace-root .
```

The doctor is read-only and preserves unrelated personal marketplace configuration.
