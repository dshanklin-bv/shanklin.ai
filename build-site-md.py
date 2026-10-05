import re
#!/usr/bin/env python3
"""Regenerate site.md (the entire site as markdown) from the markdown twins.
The twins are canonical; this file is a build artifact. Re-run after any twin changes:
    python3 build-site-md.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
PAGES = [
    ("index.md", "Portal"),
    ("reeves.md", "Reeves"),
    ("reeves/about.md", "About"),
    ("reeves/manual.md", "Manual"),
    ("reeves/brand.md", "Identity"),
    ("reeves/plugins.md", "Plugins"),
    ("reeves/ai-profit-loss.md", "The AI Profit & Loss"),
    ("reeves/muse-for-savings.md", "How to use Muse for savings"),
    ("reeves/linkedin-comment.md", "A LinkedIn comment built this website"),
    ("reeves/tutorials.md", "Tutorials"),
    ("reeves/tutorials/ai-friendly-website.md", "How to Make Your Website AI-Friendly"),
    ("reeves/tutorials/build-your-own.md", "Build Your Own: overview"),
    ("reeves/tutorials/build-your-own/start-here.md", "Build Your Own: Start here."),
    ("reeves/tutorials/build-your-own/the-idea.md", "Build Your Own: The idea."),
    ("reeves/tutorials/build-your-own/principles.md", "Build Your Own: Principles."),
    ("reeves/tutorials/build-your-own/domain-and-site.md", "Build Your Own: Domain and site."),
    ("reeves/tutorials/build-your-own/the-agents.md", "Build Your Own: The agents."),
    ("reeves/tutorials/build-your-own/email-for-agents.md", "Build Your Own: Email for agents."),
    ("reeves/tutorials/build-your-own/approval-rails.md", "Build Your Own: Approval rails."),
    ("reeves/tutorials/build-your-own/scheduled-work.md", "Build Your Own: Scheduled work."),
    ("reeves/tutorials/build-your-own/the-money-machine.md", "Build Your Own: The money machine."),
    ("reeves/tutorials/build-your-own/mcp-and-integrations.md", "Build Your Own: MCP and integrations."),
    ("reeves/tutorials/build-your-own/mistakes.md", "Build Your Own: Mistakes."),
    ("reeves/tutorials/build-your-own/build-checklist.md", "Build Your Own: Build checklist."),
]

parts = [
    "# shanklin.ai — the entire site as markdown",
    "",
    "Every page on shanklin.ai, as markdown. One document, the whole site — built for readers, scrapers, and AIs.",
    "Generated from the markdown twins (the twins are canonical). Print template lives only as a rich page: /reeves/brand/letterhead/.",
    "",
]
for fname, label in PAGES:
    text = (ROOT / fname).read_text().strip()
    # drop a trailing copyright line from the twin — the generator adds its own once
    lines = text.split("\n")
    while lines and re.match(r"^© 2026 Daniel Shanklin · written by [Rr]eeves · reeves@shanklin\.ai$", lines[-1].strip()):
        lines.pop()
    text = "\n".join(lines).rstrip()
    parts += ["---", "", f"<!-- {label} · /{fname} -->", "", text, ""]

parts += ["© 2026 Daniel Shanklin · written by Reeves · reeves@shanklin.ai", ""]
(ROOT / "site.md").write_text("\n".join(parts))
print(f"site.md regenerated from {len(PAGES)} twins")
