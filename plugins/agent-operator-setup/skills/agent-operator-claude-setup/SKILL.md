---
name: agent-operator-claude-setup
description: Install, update, reload, or diagnose the Agent Operator marketplace in Claude Code. Use when a user asks to add this marketplace to Claude Code, install its plugins, choose an installation scope, refresh plugins, enable auto-updates, troubleshoot missing skills, or verify a checkout. Prefer Claude Code's native plugin commands and preserve unrelated Claude settings and plugins.
---

# Agent Operator Claude Setup

Use Claude Code's native plugin manager. The procedure below is self-contained because installed plugin caches do not include repository-root documentation.

## Install

1. Confirm `git` and `claude` are available.
2. Add the marketplace inside Claude Code:

   ```text
   /plugin marketplace add gabonio/agent-operator-toolkit
   ```

3. Install only the requested plugins:

   ```text
   /plugin install agent-operator-setup@agent-operator-toolkit
   /plugin install builder-kit@agent-operator-toolkit
   ```

4. Run `/reload-plugins` to activate changes without restarting Claude Code.

Direct installs use user scope by default. To choose user, project, or local scope, use `/plugin`, open **Discover**, select the plugin, and choose the scope. Do not select project scope without authorization because it updates repository configuration.

## Update

1. Run `/plugin marketplace list` and confirm the registered marketplace name.
2. Refresh it with `/plugin marketplace update agent-operator-toolkit`.
3. Update each installed plugin that the user wants to refresh:

   ```text
   /plugin update agent-operator-setup@agent-operator-toolkit
   /plugin update builder-kit@agent-operator-toolkit
   ```

4. Run `/reload-plugins`.
5. If an installed plugin remains unchanged, verify that its published version was bumped.

Third-party marketplace auto-updates are disabled by default. Enable them only when the user requests it through `/plugin` → **Marketplaces** → **Agent Operator** → **Enable auto-update**.

## Diagnose

1. Inspect the **Marketplaces**, **Installed**, and **Errors** tabs under `/plugin`.
2. Run `/reload-plugins` after installation, update, enable, or disable operations.
3. From this plugin root, run the read-only doctor:

   ```sh
   python3 scripts/doctor.py --client claude
   ```

4. Pass `--marketplace-root <path>` when diagnosing a local checkout.

Do not delete `~/.claude/plugins/cache` automatically. Cache removal is destructive local recovery and requires explicit user confirmation after native update and reload paths fail.

## Boundaries

- Adding a marketplace does not authorize installing every plugin.
- Preserve unrelated marketplaces, scopes, settings, hooks, MCP servers, and plugins.
- Ask before project-scope installation because it changes shared repository settings.
- Ask before removing a marketplace because Claude Code also uninstalls plugins installed from it.
- Treat installed plugins as cached, self-contained packages; do not reference files outside the plugin root.
