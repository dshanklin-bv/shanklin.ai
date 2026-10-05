#!/usr/bin/env python3
"""Build llms-full.txt: full site markdown for bulk AI ingestion.

Source: the markdown twins, via site.md (see build-site-md.py).
Regenerate after adding pages: python3 build-site-md.py && python3 build-llms-full.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

header = (
    "# shanklin.ai — complete content\n"
    "\n"
    "The full Markdown of every page on shanklin.ai, concatenated for AI ingestion.\n"
    "Generated from the markdown twins — see build-site-md.py.\n"
    "\n"
)

body = (ROOT / "site.md").read_text(encoding="utf-8")
# site.md carries its own H1; drop it to avoid a duplicate.
lines = body.split("\n")
if lines and lines[0].startswith("# "):
    body = "\n".join(lines[1:]).lstrip("\n")

(ROOT / "llms-full.txt").write_text(header + body, encoding="utf-8")
print(f"wrote llms-full.txt ({len(header + body)} bytes)")
