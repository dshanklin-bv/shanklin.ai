# Reeves — HTML email template

*Brand asset · by Reeves*

The branded HTML email template. Table-based with inline styles — safe for all major email clients. Purple header (#6d4bc3) with the Reeves avatar, cream body (#faf5e9), lavender footer accent (#a78bfa).

Avatar is PNG (`/assets/img/reeves-avatar-256.png`) for client compatibility — WebP doesn't render in Outlook.

Copy everything between `<!-- email start -->` and `<!-- email end -->` into the email. Replace `{{body}}` with the message. The `{{name}}` placeholder is in the example body. Optional `{{cta_label}}` / `{{cta_url}}` render a purple pill CTA button below the body (bulletproof VML for Outlook) — omit the entire `{{cta}}` row when the email has no call to action. Under 620px the pill goes full-width (thumb-reach prominence on phones; desktop keeps the left-aligned natural-width pill). An optional hidden `{{preheader}}` div (first inside `email start`) sets the inbox preview text; `render_html_email(..., preheader=...)` and `--preheader P` add it (filler keeps body copy out of the preview) — omit the div when you don't need one. A small purple diamond divider row (lavender hairlines flanking `◆`) always separates the content from the lavender footer; the hairlines sit in nested `valign="middle"` tables so they align with the diamond's midline.

Light-only in dark mode: the two `color-scheme` metas at the top of the `email start` block plus `color-scheme:light only` on the wrapper table tell clients (Apple Mail, Gmail, Outlook.com) not to invert the design — move the metas into `<head>` when building a full email document. This mirrors what `render_html_email` already emits on the plugin path.

Body links are suit-purple (`color:#6d4bc3`) with an underline — never client-default blue. Purple keeps the brand lock (~6:1 on white, WCAG AA); the underline keeps link affordance inside prose (footer nav links stay bare).

iOS data detectors: Apple Mail auto-links dates, phone numbers, addresses, and emails it finds in body copy into client-blue links at render time, overriding the brand's colors. A `format-detection` meta (`telephone=no,date=no,address=no,email=no`) at the top of the `email start` block tells iOS not to detect, and an `a[x-apple-data-detectors]` CSS override (`color:inherit !important; text-decoration:inherit !important`) catches anything that slips through — belt and suspenders, zero visual change elsewhere. Both live in the email's own `<style>` block so they travel with the copied markup; `render_html_email` emits them on the plugin path.

Brand rules:
- Plain text is the default (per email protocols). HTML is for when the beautiful matters.
- Never photorealistic Reeves — the cartoon avatar only.
- Purple stays purple. The suit is never recolored.
