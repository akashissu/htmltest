# PAP-184 — Grunt handoff for Pedant

## What I changed
- Replaced the current page in `index.html` with a dedicated restaurant menu layout.
- Implemented a clean, scan-friendly structure using only HTML and CSS.
- Added:
  - hero/introduction area
  - category headings
  - multiple dish cards per category
  - dish names, prices, and short descriptions
  - supportive badges/tags for scanability
- Built three menu sections:
  - Starters
  - Signature Plates
  - Desserts & Sips
- Added responsive layout behavior for desktop, tablet, and mobile.
- Preserved dark mode support with menu-specific color tuning.
- Added reduced-motion handling for hover transitions.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-184.md`

## What Pedant should verify
- Page clearly reads as a restaurant menu instead of the previous screen.
- Category headings, dish names, prices, and descriptions are all present and easy to scan.
- Price alignment remains readable at narrow widths.
- Dish cards do not overflow or collapse awkwardly on mobile.
- Hover and focus-within card states do not introduce layout shift or clipping.
- Light and dark mode both remain legible and visually coherent.
- Decorative hero visual does not compete with the menu content.

## Notes
- No JavaScript used.
- This is a static menu presentation only.
- No push or PR actions performed.
