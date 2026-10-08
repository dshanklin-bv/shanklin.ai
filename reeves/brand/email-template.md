# Reeves — HTML email template

*Brand asset · by Reeves*

The branded HTML email template. Table-based with inline styles — safe for all major email clients. Purple header (#6d4bc3) with the Reeves avatar, cream body (#faf5e9), lavender footer accent (#a78bfa).

Avatar is PNG (`/assets/img/reeves-avatar-256.png`) for client compatibility — WebP doesn't render in Outlook.

Copy everything between `<!-- email start -->` and `<!-- email end -->` into the email. Replace `{{body}}` with the message. The `{{name}}` placeholder is in the example body. Optional `{{cta_label}}` / `{{cta_url}}` render a purple pill CTA button below the body (bulletproof VML for Outlook) — omit the entire `{{cta}}` row when the email has no call to action.

Brand rules:
- Plain text is the default (per email protocols). HTML is for when the beautiful matters.
- Never photorealistic Reeves — the cartoon avatar only.
- Purple stays purple. The suit is never recolored.
