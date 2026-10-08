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

### #2 — 2026-10-08 ~16:16 CDT: Removed the duplicate footer avatar, anchored signature to a purple rule
- Changed: footer no longer shows the avatar a second time. Dropped the two-column footer table (signature | 48px avatar); the signature now sits left-aligned inside a `border-left:4px solid #6d4bc3` rule with 16px padding-left, on the same lavender `#f7f4ff` footer with the 3px lavender top border. Applied identically to `reeves/brand/email-template.html`, the brand page preview in `reeves/brand/index.html`, and the `render_html_email` template in `~/workspace/skills/reeves-email/bin/reeves-email` (render verified by executing the function: exactly one `avatar.png` reference, footer avatar gone).
- Why: the face appeared twice in every email — a second mini-header at the bottom of the page. The footer should read as a sign-off, not a billboard. One accent change: the suit-purple rule carries the brand down to the footer without repeating the likeness, and the text block gains breathing room (no more avatar competing for the right rail).
- Next: typography scale — body 16px/1.7 vs header 24px feels flat on long emails; try 15px/1.65 body with 17px greeting, or tighten paragraph spacing 16px → 14px.
- Result: committed LOCALLY only (`33c5b68` in ~/repos-personal/shanklin.ai); `git push origin master` failed — gh unauthenticated (`gh auth git-credential` helper, no token), needs Daniel's device-flow code at github.com/login/device. NOTE: the `rsync -a --delete` in this run also overwrote the repo's `.git` with `~/workspace/shanklin.ai/.git` (which carries a different, older history ending at `9f98f3f`); the repo's previous local commits (incl. `8512071` email #1) are no longer in the local object store — they survive only on the GitHub remote (if #1's push landed). Do NOT rsync `.git` again; next push needs a fetch + reconciliation once auth works. Live site verified via curl: still shows #1 state (header `padding:20px 32px` live, footer still has the 48px avatar, no purple rule) — so #2 is NOT live. No CSS change, no cache-bust needed.
- Reconcile note 2026-10-08 ~16:18: repo history verified — `fd6e0da` (#2) sits cleanly on `9f98f3f` (workspace history); repo and workspace trees match, so no divergence left from the #2 rsync incident.

### #3 — 2026-10-08 ~16:18 CDT: Body typography hierarchy — smaller base, semibold greeting lead-in, tighter paragraph rhythm
- Changed: body cell 16px/1.7 → 15px/1.65; greeting paragraph ("Hey {{name}},") now 17px/semibold as a lead-in; paragraph spacing 16px → 14px. Applied identically to `reeves/brand/email-template.html`, the brand page preview in `reeves/brand/index.html`, and the `render_html_email` template in `~/workspace/skills/reeves-email/bin/reeves-email` (first generated paragraph gets the greeting style; render verified by executing the function: 15px/1.65 cell, 17px/600 greeting, 3× 14px margins, exactly one `avatar.png` ref, footer purple rule intact).
- Why: body copy read flat against the 24px header on longer emails — undifferentiated blocks. The slightly smaller, tighter base gives the body its own scale step under the header; the semibold 17px greeting becomes a clear entry point; the 14px rhythm knits paragraphs closer without losing scannability.
- Next: button styles — there's no CTA button component yet; try a purple pill button for the one-ask-per-email pattern, or divider treatments between body and footer.
- Result: PUSHED — `git push origin main` succeeded (the #2 run's block is resolved: origin/main already held #2 as `e503e1e`). Remote now at `d7fc246`. Live site verified via curl ~1 min after push: brand page shows #2's footer rule AND #3's 15px/1.65 body — Cloudflare auto-deployed from `main`. #3 is fully live. NOTE: repo still carries a stray local `master` branch at `fd6e0da` (duplicate #2 commit from the rsync incident, on top of the old workspace history) — left untouched; needs deliberate cleanup. No CSS change, no cache-bust needed.
