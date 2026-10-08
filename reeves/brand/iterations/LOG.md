# Email Template Iteration Log

Goal: iterate the Reeves HTML email template every 5 minutes until Daniel loves the full identity with images.

## Rules
- ONE focused change per iteration. Not a redesign — a refinement.
- Each entry: what changed, why, and what to try next.
- Brand locks: purple (#6d4bc3), never photorealistic, cartoon avatar only.
- Email must stay table-based, inline styles, light-only, high contrast.
- Push live after every iteration so Daniel sees it.

## Iterations

### #1 — 2026-10-08 ~16:10 CDT: Tightened header proportions
- Changed: header vertical padding 28px → 20px; avatar 64px → 72px (cell width 72 → 80 to hold the 3px ring). Applied identically to `reeves/brand/email-template.html`, the brand page preview in `reeves/brand/index.html`, and the `render_html_email` template in `~/workspace/skills/reeves-email/bin/reeves-email`.
- Why: the header was top-heavy — ~120px of purple slab with a small avatar floating in it. Tightening the slab and enlarging the character shifts visual weight to Reeves himself and gets the reader into the body copy faster. One cohesive proportions change, no redesign.
- Next: footer layout — the footer avatar duplicates the header one (avatar appears twice in every email); try dropping the footer avatar and left-aligning signature text against a small purple rule, or enlarging footer breathing room.
- Result: committed, pushed; live via Cloudflare Pages. No CSS change, no cache-bust needed.
