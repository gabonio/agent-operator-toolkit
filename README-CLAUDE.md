# Agent Operator for Claude Code

This guide installs, updates, and troubleshoots Agent Operator in Claude Code using Claude's native plugin marketplace commands.

## Quick install

Run these commands inside Claude Code:

```text
/plugin marketplace add gabonio/agent-operator-toolkit
/plugin install agent-operator-setup@agent-operator-toolkit
/plugin install builder-kit@agent-operator-toolkit
/reload-plugins
```

Adding the marketplace makes its catalog available; it does not install every plugin. Install only the plugins you want. `marketplace-management` is useful for people who maintain plugin marketplaces:

```text
/plugin install marketplace-management@agent-operator-toolkit
/reload-plugins
```

The default installation scope is user scope. To choose user, project, or local scope interactively, run `/plugin`, open **Discover**, select the plugin, and choose the scope.

## Easy setup command

After installing `agent-operator-setup`, run:

```text
/agent-operator-setup:setup install
```

The same command supports:

```text
/agent-operator-setup:setup update
/agent-operator-setup:setup doctor
```

## Update

Refresh the marketplace and installed plugins:

```text
/plugin marketplace update agent-operator-toolkit
/plugin update agent-operator-setup@agent-operator-toolkit
/plugin update builder-kit@agent-operator-toolkit
/reload-plugins
```

The marketplace update refreshes the catalog; each `/plugin update` refreshes an installed plugin. Update `marketplace-management` the same way if it is installed.

Third-party marketplace auto-updates are disabled by default. To enable them, run `/plugin`, open **Marketplaces**, select **Agent Operator**, and choose **Enable auto-update**.

These plugins use explicit versions. A published change must bump the plugin version before Claude Code will download it as an update.

## Diagnose

Start with Claude Code's plugin manager:

1. Run `/plugin`.
2. Check **Marketplaces** for `agent-operator-toolkit`.
3. Check **Installed** for the plugin and its selected scope.
4. Check **Errors** for loading or path failures.
5. Run `/reload-plugins` after installing, enabling, disabling, or updating plugins.

The setup plugin also includes a read-only doctor. From the plugin root, run:

```sh
python3 scripts/doctor.py --client claude
```

For a local checkout:

```sh
python3 plugins/agent-operator-setup/scripts/doctor.py --client claude --marketplace-root .
```

The doctor does not install plugins, edit Claude settings, or delete caches.

## Remove or disable

Disable a plugin without uninstalling it:

```text
/plugin disable builder-kit@agent-operator-toolkit
```

Remove a plugin completely:

```text
/plugin uninstall builder-kit@agent-operator-toolkit
```

Removing the marketplace also uninstalls plugins installed from it:

```text
/plugin marketplace remove agent-operator-toolkit
```

## Security and recovery

- Install only plugins and marketplaces you trust; plugins can execute with your user permissions.
- Do not manually rewrite `~/.claude` configuration while native marketplace commands work.
- Ask before deleting plugin caches. Cache deletion removes local state and is a last-resort recovery step.
- Installed plugins are copied into Claude Code's cache and cannot reference files outside their own plugin directory.

For the current command reference, see Anthropic's [plugin discovery guide](https://code.claude.com/docs/en/discover-plugins) and [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces).
