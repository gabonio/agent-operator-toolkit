---
name: agent-operator-gemini-setup
description: Install, update, restart, or diagnose Agent Operator as a Gemini CLI extension. Use when a user asks to install the extension from GitHub or a local checkout, enable auto-update, refresh skills or commands, troubleshoot extension discovery, or remove the extension. Prefer native Gemini extension commands and preserve unrelated Gemini settings and extensions.
---

# Agent Operator Gemini Setup

Gemini CLI installs Agent Operator as one extension containing the marketplace's portable skills and commands.

## Install

Run from a terminal, outside the Gemini interactive session:

```sh
gemini extensions install https://github.com/gabonio/agent-operator-toolkit
```

Add `--auto-update` only when the user requests automatic updates. For local development, use `gemini extensions link <checkout-path>` instead of copying files into `~/.gemini` manually.

Restart Gemini CLI after installation. Inside Gemini, verify the extension and reload its components:

```text
/extensions list
/skills reload
/commands reload
```

The setup command is `/agent-operator:setup`.

## Update

Run from a terminal:

```sh
gemini extensions update agent-operator-toolkit
```

Then restart Gemini CLI. Extension management changes take effect after restart.

## Diagnose

1. Run `gemini extensions list` in a terminal or `/extensions list` interactively.
2. Confirm the extension is enabled and its version/source are expected.
3. Run the read-only doctor from this checkout or extension root:

   ```sh
   python3 plugins/agent-operator-setup/scripts/doctor.py --client gemini --marketplace-root .
   ```

4. Use `/skills list`, `/commands list`, `/skills reload`, and `/commands reload` to inspect discovery.

## Remove or disable

Use native commands:

```sh
gemini extensions disable agent-operator-toolkit --scope user
gemini extensions enable agent-operator-toolkit --scope user
gemini extensions uninstall agent-operator-toolkit
```

## Boundaries

- Installing or linking an extension changes user-level state and requires user intent.
- Do not pass `--consent`, enable auto-update, or choose a workspace scope unless requested.
- Preserve unrelated Gemini extensions, settings, skills, commands, hooks, agents, and MCP servers.
- Ask before deleting `~/.gemini/extensions` content or replacing extension metadata.
