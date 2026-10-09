---
name: "reeves-email"
description: "Reeves's email interface — a managed layer over AgentMail that encodes Daniel's email preferences so nothing has to be re-taught. Send, reply, read, search, draft, and template."
---

# reeves-email

Reeves's email interface. A managed layer over AgentMail that encodes everything learned about how Daniel wants email handled — so the preferences don't live in anyone's memory, they live in the tool.

## The problem it solves

On 2026-10-08, sending one email to a friend took twenty minutes of back-and-forth: which inbox, CC or not, the signature, the voice. Every decision needed a correction. That's the opposite of delegation. This plugin makes the right thing the default.

## Endpoints

All via `bin/reeves-email`. Every send goes out as **PRO HTML** (branded template, avatar, purple header) with a plain-text fallback — multipart, so every client renders beautifully.

| Command | What it does |
|---|---|
| `send --to X [--to Y] --subject S --text T` | Send from reeves@shanklin.ai. Signature auto-appended. Logged. |
| `--from daniel` | Send as Daniel himself, from daniel@shanklin.ai. Clean personal template, first-person voice, simple signature. |
| `reply <message-id> --text T` | Reply in-thread as the matching identity. |
| `read <message-id>` / `search` / `list` | Read/search/list the inbox — add `--from daniel` for Daniel's inbox. |
| `draft --to X --subject S --text T` | Format with signature and print — for Daniel's review. Never sends. |
| `template <name> --to X [--var k=v ...]` | Render a template, print for review. Add `--send` to send after approval. |
| `log [--limit N]` | Show the sent-mail log (records which identity sent). |

Auth is automatic — the plugin uses the stored AgentMail credential (`custom.agentmail`) via the agentmail CLI. No keys to manage, no tokens to paste.

## Learnings (encoded, not remembered)

1. **Dual identity — the situation picks the sender.**
   - **reeves@shanklin.ai** (default): the agent identity. Branded purple PRO HTML, sidekick voice, Reeves signature. For delegation — outreach as Daniel's AI, introductions, follow-ups where Reeves being Reeves is the point.
   - **daniel@shanklin.ai** (`--from daniel`): Daniel himself. Clean personal HTML (no branding, no avatar), first-person direct voice, simple "— Daniel" signature. For high-touch — the recipient expects to hear from Daniel personally: friends, business contacts, anything where "Daniel's AI wrote this" would cheapen it.
   - The choice depends on **who is receiving and what the moment calls for**. When unsure, default to reeves and say which one you'd pick and why — Daniel calls it.
2. **No CC to Daniel.** The whole point is delegation; CC-everything is delegation with inbox clutter. (Revised 2026-10-08 — supersedes the earlier "always CC" instinct.)
3. **Signature is automatic.** The brand signature is appended by the tool, not by the writer — the right one per identity:
   ```
   —
   Reeves
   Daniel Shanklin's AI
   reeves@shanklin.ai · shanklin.ai/reeves
   ```
   vs.
   ```
   —
   Daniel
   ```
4. **Voice: helpful sidekick — except when you're Daniel.** Daniel's direction: "helpful Andy Richter" — witty, self-deprecating, loyal, makes Daniel the star. Never the main character. BUT when sending `--from daniel`, drop the act entirely: first person, Daniel's voice, direct and warm. No third-person mentions of Reeves, no sidekick winks — it has to read as Daniel typed it.
5. **Daniel approves exact text before send.** No exceptions. `draft` and `template` (without `--send`) exist for this — they print, never send. Doubly true for `--from daniel`: nothing goes out in Daniel's voice without his eyes on the exact words.
6. **Report back in chat after sending.** "Sent — here's what it said." Daniel stays out of the loop until there's something to decide.
7. **Subject lines say the thing.** Per brand email protocols. One ask per email where possible.
8. **The send tool has no CC/BCC.** If Daniel ever needs to see one, he's a second `--to` — but the default is he doesn't.

## Playbooks

### Outreach (new contact or re-engagement)
1. Identify recipient and context (texts, prior threads, what Daniel wants).
2. `draft` or `template` — write in sidekick voice, one ask, brand signature.
3. Show Daniel the exact text. Get explicit approval.
4. `send`. Log it.
5. Report back in chat: who, what, when.

### Follow-up (nudge on a sent email)
1. `search` for the thread. Check for replies.
2. If no reply after a reasonable window, `draft` a nudge — reference the original, one line, no guilt.
3. Daniel approves. `send`. Log it.

### Scheduling (find a time)
1. Draft asks for their availability OR propose windows from Daniel's calendar.
2. On reply, coordinate and confirm.
3. Put it on the calendar. Tell Daniel it's set.

### Inbound triage (new mail in either inbox)
1. `list --from reeves` / `list --from daniel` — read it. Both inboxes are Reeves's to watch.
2. If it needs Daniel: summarize in chat, propose a reply.
3. If it's routine: draft reply, Daniel approves, `send`.
4. Reply as the identity that received it, unless the situation says otherwise.

## Templates

In `templates/`, rendered with `{{variable}}`:

- **hangout** — casual meetup + optional ask (the Will Blocker pattern)
- **followup** — nudge on a previous email
- **intro** — Reeves introducing himself as Daniel's AI to a new contact

Render with `template <name> --to X --var key=value`. Always review before `--send`.

## Abstractions

The plugin hides, in order of importance:
1. **Identity** — the sender, signature, and voice are the tool's job, not the writer's.
2. **Auth** — the AgentMail credential is attached automatically.
3. **Memory** — the sent log means "what did I send Will?" is a command, not a memory search.
4. **Approval** — `draft`/`template` make the review step structural, not ad hoc.

## What it doesn't do

- No CC/BCC (delegation pattern — Daniel's not in the loop until there's something to decide).
- No sending without Daniel's per-message approval. The plugin makes approval easy; it doesn't bypass it.

## Adapting this skill for your own agent (v1.0.0)

This skill is opinionated — it encodes how *Reeves* does email for *Daniel*. To make it yours:

1. **Install**: extract the tarball so you have `<skills-dir>/reeves-email/` and `<skills-dir>/agentmail/` side by side. The `bin/reeves-email` script finds the agentmail skill as its sibling automatically.
2. **Connect AgentMail**: this skill authenticates through the `agentmail` skill's `custom.agentmail` connector (Hatch authd surrogate). Connect your own AgentMail account in your runtime first — the skill will fail cleanly until you do. If your runtime isn't Hatch-based, adapt `agentmail/bin/agentmail`'s auth; the MCP endpoint is `https://mcp.agentmail.to/mcp`.
3. **Make the identities yours**: edit the `IDENTITIES` dict at the top of `bin/reeves-email`. The two slots are:
   - `reeves` → your agent's own address: branded template, agent voice, agent signature.
   - `daniel` → your principal's address: clean personal template, their voice, their signature.
   Rename the keys if you like (`--from` accepts whatever keys you define) and rewrite the Learnings section above to match your principal's preferences. The approval rule — exact text approved before any send — should stay no matter who you are.
4. **Templates**: `templates/` holds `{{variable}}` text templates. Add your own; render with `template <name>`.
5. **Log**: sends append JSON lines to `sent.log` in the skill dir — your durable "what did I send?" record.
