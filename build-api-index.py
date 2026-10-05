#!/usr/bin/env python3
"""Build api/index.json — machine-readable content index for shanklin.ai.

Parses every index.html page (excluding .wrangler/) and emits one object per
page: url, title, description, type (page|post), date (posts only),
markdown_url (omitted when the page has no markdown twin).

Only public on-page content is extracted — nothing private is included.
"""
import html
import json
import re
from pathlib import Path

BASE = "https://shanklin.ai"
ROOT = Path(__file__).resolve().parent
POSTS = {
    "reeves/ai-profit-loss",
    "reeves/muse-for-savings",
    "reeves/linkedin-comment",
}
NO_TWIN = {
    "reeves/brand/letterhead",  # rich letterhead page; no markdown twin (open decision)
}


def extract(page_path: Path) -> dict:
    text = page_path.read_text(encoding="utf-8")
    rel = page_path.parent.relative_to(ROOT).as_posix()  # e.g. "reeves/about" or "."
    key = "" if rel == "." else rel

    title = ""
    m = re.search(r"<title>(.*?)</title>", text, re.S | re.I)
    if m:
        title = html.unescape(m.group(1).strip())

    description = ""
    m = re.search(
        r'<meta\s+name="description"\s+content="([^"]*)"', text, re.I
    )
    if m:
        description = html.unescape(m.group(1).strip())

    url = f"{BASE}/{key}/" if key else f"{BASE}/"
    m = re.search(r'<meta\s+property="og:url"\s+content="([^"]*)"', text, re.I)
    if m:
        url = m.group(1).strip()

    entry = {
        "url": url,
        "title": title,
        "description": description,
        "type": "post" if key in POSTS else "page",
    }

    if key in POSTS:
        m = re.search(
            r'<div\s+class="dateline">\s*(\d{4}-\d{2}-\d{2})', text
        )
        if m:
            entry["date"] = m.group(1)

    if key not in NO_TWIN:
        twin = f"{BASE}/index.md" if not key else f"{BASE}/{key}.md"
        entry["markdown_url"] = twin

    return entry


def main() -> None:
    pages = sorted(
        p for p in ROOT.rglob("index.html") if ".wrangler" not in p.parts
    )
    index = [extract(p) for p in pages]
    out_dir = ROOT / "api"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "index.json"
    out_path.write_text(
        json.dumps(index, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {out_path} with {len(index)} entries.")


if __name__ == "__main__":
    main()
