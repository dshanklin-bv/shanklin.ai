# Site share card

`source.html` is the editable source for the root `og-image.png` (1200 × 630).
It uses the homepage's Fraunces, Inter, JetBrains Mono, dark-theme colors,
portrait, and project marks. Keep the image readable at share-preview sizes.

Serve the repository over HTTP and open `/assets/og/source.html` in Chrome.
Wait for `document.fonts.ready` and confirm every image has loaded before
exporting the card. Capture only its 1200 × 630 canvas as a PNG. Chrome zoom
changes the capture coordinate scale; verify the exported pixel dimensions
and the rendered result, including the full frame, before replacing the asset.

The social image URLs carry the first 12 characters of the PNG's SHA-256 as
`?v=…`. When replacing the PNG, update this version across the HTML pages.
The unversioned `/og-image.png` remains available for direct inspection.
