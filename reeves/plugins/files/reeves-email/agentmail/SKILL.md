---
name: "agentmail"
description: "Use Agentmail when the user asks for Agentmail or this provider's API."
---

# Agentmail

## Purpose
Use Agentmail with the user-connected `custom.agentmail` credential.

## Tooling
Service CLIs live under `~/workspace/skills/agentmail/bin/`:

- `bin/agentmail` — full CLI over the hosted MCP server (`https://mcp.agentmail.to/mcp`).
  Uses `bin/dynamic_credentials.py` (authd surrogate for `custom.agentmail`); never
  handles raw secrets. Commands:
  - `agentmail inboxes` — list all inboxes
  - `agentmail messages <inbox> [--limit N] [--label L]` — list messages
  - `agentmail read <inbox> <message-id>` — full message body
  - `agentmail search <inbox> <query>` — full-text search
  - `agentmail send <inbox> --to a@b.c [--to ...] --subject S --text T` — send
  - `agentmail reply <inbox> <message-id> --text T [--reply-all]` — reply

MCP tool params are camelCase (`inboxId`, `messageId`, `q`). Key inboxes:
`reeves@shanklin.ai` ("Reeves - Daniels AI assistant"), `reeves@agentmail.to`.
Domain mail for shanklin.ai flows through Amazon SES
(MX `inbound-smtp.us-east-1.amazonaws.com`, verified 2026-10-04).

CLIs must use authd or shared connector helpers for authenticated requests. They must not read OAuth client credentials, browser callback payloads, refresh tokens, access tokens, or Muse auth files directly.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, call `credentials.request_api_access` with `reconnect` to replace it. The connector is stored as `custom.agentmail`.

## Operating Rules
1. Use this skill when the user asks for Agentmail or this provider's API.
2. Restrict authenticated requests to: mcp.agentmail.to.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.
5. Reading the inbox is always fine. Sending or replying needs Daniel's per-message
   approval, like any other outward communication.
6. Do NOT set up Cloudflare Email Routing for shanklin.ai — it would conflict with
   the working SES MX records.
