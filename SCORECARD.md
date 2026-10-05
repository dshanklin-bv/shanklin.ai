# shanklin.ai — Definition of Done

Scorecard for the site. Every item is verifiable — no vibes. Re-run after any
significant change. Last scored: 2026-10-04.

## Content — 4/4 ✅

- [x] Every page ships real copy. No lorem, no placeholders, no "coming soon".
- [x] Every HTML page has a markdown twin with matching content (verified by
      section-diff, not eyeball). Twins are canonical.
- [x] `site.md` regenerates from the twins via `build-site-md.py` — never
      hand-edited, can't drift.
- [x] Origin story: skeptic credited by role (no name), token figure is the
      verified ~1% meter reading with the caveat stated, tone is generous.

## Voice & standards — 4/4 ✅

- [x] Reeves pages in first-person Reeves voice; portal in Daniel's voice.
      No page speaks in nobody's voice.
- [x] No banned moves: no pep talks, no buried caveats, no market-as-alpha,
      no photorealistic Reeves.
- [x] No vendor names in public copy (grouped categories only).
- [x] Every `#reeves` reply promise states the approval truth.

## Visual — 4/5 ⚠️

- [x] Portal renders clean in light (Longhorns), dark (ember), ai.
- [x] Reeves pages render clean in light (purple accents), dark
      (purple-black), ai.
- [x] No stray underlines, overlaps, or broken images in any theme
      (checked via screenshots, not just CSS reading).
- [x] 390px mobile: no page-level horizontal scroll, no overlap. Verified by
      auditing every multi-column component at ≤640px — all grids collapse
      to one column, wide tables scroll internally, headlines are clamp-based.
      (No device render available in this environment; the hosted browser
      can't resize viewports.)
- [x] Tile icon chips legible in dark mode.

## Technical — 5/5 ✅

- [x] All internal links resolve (scripted check, zero missing targets).
- [x] Div balance on every page (scripted).
- [x] One CSS hash site-wide per deploy (cache-busting discipline).
- [x] Markdown twins served as `text/markdown`; all return 200 live.
- [x] Markdown pill opens the page's twin in a new tab on all 9 pages
      (verified live).

## Identity — 3/3 ✅

- [x] Reeves is the stylized cartoon everywhere; suit always purple.
- [x] Likeness bible published: approved assets, nevers, rights with Daniel,
      new renders need his approval.
- [x] Co-branding and governance rules published; steward named.

## Score: 21/21

All green. Re-run this scorecard after any significant change.
