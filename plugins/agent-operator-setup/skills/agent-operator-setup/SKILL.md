---
name: agent-operator-setup
description: Agent-neutral setup router for installing, updating, or diagnosing Agent Operator in Codex, Claude Code, or Gemini CLI. Use when the user asks to set up Agent Operator without naming a client, wants the correct native installation path, or needs cross-client troubleshooting. Discover the active client, route to its owning setup skill, and preserve unrelated user configuration.
---

# Agent Operator Setup

Use this skill as a thin, agent-neutral router. Do not pretend the three clients share one installation format.

1. Determine whether the target is Codex, Claude Code, or Gemini CLI from the user's request and available executable.
2. If more than one client is plausible and the requested action would mutate user configuration, ask which client is in scope.
3. Read and follow only the matching setup skill:

   | Client | Owning skill |
   | --- | --- |
   | Codex | [Codex setup](../agent-operator-codex-setup/SKILL.md) |
   | Claude Code | [Claude setup](../agent-operator-claude-setup/SKILL.md) |
   | Gemini CLI | [Gemini setup](../agent-operator-gemini-setup/SKILL.md) |

4. Prefer the client's native marketplace or extension commands.
5. Use read-only diagnosis before changing user-level state.

Adding a marketplace or extension does not authorize installing every component. Preserve unrelated plugins, extensions, skills, agents, commands, hooks, MCP servers, scopes, and configuration.
