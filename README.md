# Agent Operator

**A portable marketplace of professional software-development skills for Codex, Claude Code, and Gemini CLI.**

[![Codex](https://img.shields.io/badge/Codex-native-111827)](./README-CODEX.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-native-D97757)](./README-CLAUDE.md)
[![Gemini CLI](https://img.shields.io/badge/Gemini_CLI-native-4285F4)](./README-GEMINI.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)

Agent Operator gives coding agents a reusable operating system for planning, implementation, verification, and review. Install the same workflows through each agent's native extension model—without depending on an employer-specific service, proprietary review bot, or private convention.

The flagship **Builder Kit** plugin combines specification-driven development, repository-aware engineering rules, specialist review lenses, safe Git workflows, and a bounded adversarial review loop that keeps working until a change is genuinely merge-ready.

## Why Agent Operator?

- **One workflow, three agents.** Codex, Claude Code, and Gemini CLI receive equivalent skills through their native distribution formats.
- **Built for real repositories.** Skills discover local instructions, architecture, checks, and constraints before proposing changes.
- **Review that pushes back.** The adversarial loop surfaces three or four material findings per pass, verifies them, fixes authorized issues, and reviews the complete diff again.
- **Safe by default.** Installation, Git, GitHub, credentials, and destructive actions retain explicit authority boundaries.
- **Portable by design.** No company names, internal commands, private infrastructure, or organization-only dependencies.
- **A marketplace, not a monolith.** Install only the plugins you want and extend the catalog with self-contained skills.

## Install

Choose your agent. Each route uses that client's native marketplace or extension system.

### Codex

```sh
codex plugin marketplace add git@github.com:gabonio/agent-operator-toolkit.git
```

Restart Codex if needed, open `/plugins`, select **Agent Operator**, and install `builder-kit` or the other plugins you want.

[Complete Codex setup, updates, and troubleshooting →](./README-CODEX.md)

### Claude Code

Run inside Claude Code:

```text
/plugin marketplace add gabonio/agent-operator-toolkit
/plugin install agent-operator-setup@agent-operator-toolkit
/plugin install builder-kit@agent-operator-toolkit
/reload-plugins
```

[Complete Claude Code setup, scopes, updates, and troubleshooting →](./README-CLAUDE.md)

### Gemini CLI

Run from a terminal:

```sh
gemini extensions install https://github.com/gabonio/agent-operator-toolkit
```

Restart Gemini CLI, then run `/agent-operator:setup install` or inspect the installed capabilities with `/extensions list`, `/skills list`, and `/commands list`.

[Complete Gemini CLI setup, updates, and troubleshooting →](./README-GEMINI.md)

## Marketplace

| Plugin | What it gives your agent | Best for |
| --- | --- | --- |
| [`builder-kit`](./plugins/builder-kit) | Planning, implementation, architecture and quality lenses, verification, Git safety, and adversarial review | Building and reviewing software |
| [`agent-operator-setup`](./plugins/agent-operator-setup) | Native installation, updating, diagnosis, and recovery for all three clients | Getting a team or machine set up |
| [`marketplace-management`](./plugins/marketplace-management) | Scaffolding, registry synchronization, validation, and release discipline | Creating and publishing plugins |

### Builder Kit workflows

| Skill | Use it when you want to… |
| --- | --- |
| `$builder-kit` | Route a development task through the right workflow and specialist lenses |
| `$start-new-app` | Turn a product idea into a grounded specification and implementation plan |
| `$develop-from-spec` | Implement an approved specification with evidence-backed verification |
| `$adversarial-review` | Pressure-test a plan, architecture, diff, or readiness claim without changing it |
| `$pr-review-loop` | Review, fix, verify, and repeat until the current change is merge-ready or reaches a clear stop condition |

Client interfaces may display skill names differently, but the underlying workflow and safety rules remain aligned.

## The adversarial review loop

`$pr-review-loop` replaces organization-specific AI review automation with a local, portable workflow:

1. Discover the real diff boundary, base branch, repository rules, and available checks.
2. Review the complete current change across behavior, security, data integrity, compatibility, operations, and tests.
3. Return the three or four highest-value evidence-backed findings—never filler.
4. Fix findings when changes are authorized and run proportionate verification.
5. Recompute and review the complete diff, because fixes can expose or introduce new problems.
6. Stop only when the change is ready, an explicit decision is needed, an accepted risk remains, or the bounded iteration limit is reached.

GitHub comments and thread resolution are optional delivery actions. The core review works locally and does not require a hosted AI-review bot.

## How portability works

```text
                         Agent Operator
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
        Codex registry   Claude marketplace  Gemini extension
             │                 │                 │
             └─────────────────┼─────────────────┘
                               │
                    Self-contained plugins
                               │
              Builder Kit · Setup · Management
```

- `.agents/plugins/marketplace.json` is the Codex registry.
- `.claude-plugin/marketplace.json` is the Claude Code registry.
- `gemini-extension.json`, `commands/`, and `skills/` form the Gemini CLI extension.
- `plugins/` contains the authoritative, reusable plugin implementations.
- `AGENTS.md` is the canonical contributor instruction source; client-specific instruction files point back to it.

The repository validator ensures the registries agree, plugin manifests stay synchronized, Gemini entrypoints map to authoritative skills, semantic versions are valid, and required setup guides exist.

## Trust and safety

Agent Operator skills are instructions executed by your coding agent with the permissions available in that environment. Read and trust a plugin before installing it.

- No credentials or proprietary services are bundled.
- User configuration is preserved unless a requested setup action requires changing it.
- Destructive actions, publishing, remote comments, commits, and pushes are not implied by ordinary development work.
- Repository-specific instructions and product requirements remain authoritative in the project that owns them.
- Review findings distinguish evidence, inference, hypotheses, accepted risks, and decisions that require a person.

## Build your own plugin

1. Create a self-contained `plugins/<plugin-name>/` directory.
2. Add matching Claude and Codex manifests.
3. Register the plugin in both marketplace catalogs.
4. Expose portable skills through the Gemini extension surface.
5. Keep versions and shared metadata synchronized.
6. Run the marketplace validator:

   ```sh
   ./scripts/check
   ```

Read [the contributor instructions](./AGENTS.md) and [marketplace workflows](./WORKFLOWS.md) before making changes. Plugin-specific engineering guidance belongs inside the plugin that owns it; Builder Kit keeps its standards and review lenses under [`plugins/builder-kit/references`](./plugins/builder-kit/references).

## Repository layout

```text
agent-operator-toolkit/
├── .agents/plugins/marketplace.json   # Codex marketplace
├── .claude-plugin/marketplace.json    # Claude Code marketplace
├── gemini-extension.json              # Gemini CLI extension
├── commands/                          # Gemini CLI commands
├── skills/                            # Gemini CLI skill entrypoints
├── plugins/
│   ├── agent-operator-setup/
│   ├── builder-kit/
│   └── marketplace-management/
├── scripts/check                      # Cross-client validation
├── AGENTS.md                          # Canonical contributor instructions
├── README-CODEX.md
├── README-CLAUDE.md
└── README-GEMINI.md
```

## License

[MIT](./LICENSE) — use it, adapt it, and build better agent workflows with it.
