# PAP-185 — Grunt handoff for Pedant

## What I changed
- Replaced `index.html` with a dedicated travel destination landing page.
- Implemented a bright, welcoming layout using only HTML and CSS.
- Added:
  - hero banner with headline, supporting copy, and booking CTA
  - secondary hero action
  - highlights/stat strip
  - destination cards with short descriptions
  - lightweight destination links
- Built four destination cards:
  - Santorini
  - Kyoto
  - Bali
  - Amalfi Coast
- Used CSS-only decorative visuals for the hero and destination cards.
- Added responsive behavior for desktop, tablet, and mobile layouts.
- Preserved dark mode support and reduced-motion handling.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-185.md`

## What Pedant should verify
- Page clearly reads as a travel landing page and not a leftover prior screen.
- Hero headline, travel descriptions, destination cards, and booking button are all present.
- CTA buttons remain obvious and usable on smaller screens.
- Destination card layout stays balanced without overflow at tablet/mobile widths.
- Hover/focus states on CTAs and destination links are visible and consistent.
- Light mode feels bright and welcoming while dark mode remains readable.
- Decorative visuals do not overpower the text content.

## Notes
- No JavaScript used.
- All imagery is CSS-only / decorative.
- No push or PR actions performed.
