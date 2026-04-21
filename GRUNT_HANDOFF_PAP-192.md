# PAP-192 — Grunt handoff for Pedant

## What I changed
- Replaced `index.html` with a dedicated help center homepage.
- Implemented the page using only HTML and CSS.
- Added:
  - support hero section
  - search-style input area with accessible label
  - searchable help category cards
  - FAQ cards
  - contact/support option cards
- Added responsive behavior, hover/focus states, dark-mode support, and reduced-motion handling.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-192.md`

## What Pedant should verify
- Page clearly reads as a help center homepage rather than a leftover prior layout.
- Search UI is prominent, understandable, and remains usable at small widths.
- Categories, FAQ cards, and support options are all present.
- Card grids remain balanced across desktop, tablet, and mobile widths.
- No horizontal overflow appears at small sizes.
- Focus-visible states are clear on links, buttons, and quick-topic chips.
- Light and dark themes both remain legible and support clarity.

## Notes
- No JavaScript used.
- Search area is visual/static only, consistent with the HTML/CSS-only constraint.
- No push or PR actions performed.
