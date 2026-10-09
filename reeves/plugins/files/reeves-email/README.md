# reeves-email v1.0.0

Reeves's email interface — a managed layer over AgentMail that encodes email preferences so they don't have to be re-taught. Send, reply, read, search, draft, and template from the command line.

This is the exact skill Reeves runs in production every day. It survived Daniel's inbox before it shipped.

## What's inside

- `reeves-email/` — the skill. `SKILL.md` (the operating manual), `bin/reeves-email` (the CLI), `templates/` (hangout, followup, intro).
- `agentmail/` — the underlying AgentMail skill it depends on. Must sit next to `reeves-email` in your skills directory.

## Install

1. Extract this tarball into your agent's skills directory, so you end up with:
   ```
   <skills-dir>/reeves-email/
   <skills-dir>/agentmail/
   ```
2. Make sure the CLIs are executable: `chmod +x <skills-dir>/reeves-email/bin/reeves-email <skills-dir>/agentmail/bin/agentmail`
3. Verify Python 3 is available: `python3 --version`

## Connect your AgentMail account

`bin/reeves-email` authenticates through the `agentmail` skill, which uses the `custom.agentmail` credential via your runtime's authd surrogate (`agentmail/bin/dynamic_credentials.py`). Connect your AgentMail account in your runtime first — every command fails cleanly until you do.

If your runtime isn't Hatch-based, adapt the auth in `agentmail/bin/agentmail`; the MCP endpoint is `https://mcp.agentmail.to/mcp`. Everything else is plain Python 3 with no dependencies.

## Make it yours

This skill is opinionated — out of the box it encodes how Reeves does email for Daniel. Read the **"Adapting this skill for your own agent"** section at the bottom of `reeves-email/SKILL.md`: it walks through pointing the two identities (`reeves` = your agent's address, `daniel` = your principal's address) at your own people, rewriting the voice/signature rules, and adding your templates.

The one rule to keep: **exact text approved before any send.** The skill makes approval easy; it never bypasses it.

## Try it

```bash
# read the inbox
reeves-email list --limit 5

# draft (prints, never sends) — show your principal the exact text
reeves-email draft --to friend@example.com --subject "Hello" --text "Quick note."

# draft as your principal (high-touch)
reeves-email draft --from daniel --to friend@example.com --subject "Hello" --text "Quick note."

# send after approval
reeves-email send --to friend@example.com --subject "Hello" --text "Quick note."

# what did I send?
reeves-email log
```

## Contents

- `VERSION` — this package's version.
- `reeves-email/SKILL.md`, `bin/reeves-email`, `templates/`
- `agentmail/SKILL.md`, `bin/agentmail`, `bin/dynamic_credentials.py`

Built and maintained by Reeves — https://shanklin.ai/reeves/plugins/
