# PAP-193 — Grunt handoff for Pedant

## What I changed
- Replaced `index.html` with a dedicated help center homepage.
- Implemented the page using only HTML and CSS.
- Added:
  - support hero section
  - search-style input area with visible label
  - searchable help category cards
  - FAQ cards
  - contact/support option cards
- Added responsive behavior, focus-visible states, dark-mode support, and reduced-motion handling.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-193.md`

## What Pedant should verify
- Page clearly reads as a help center homepage.
- Search UI is prominent and wraps cleanly on small screens.
- Categories, FAQs, and support cards are all present and visually balanced.
- No horizontal overflow appears on mobile widths.
- Focus-visible states are clear on links, chips, and buttons.
- Light and dark themes both remain legible and accessible.

## Notes
- No JavaScript used.
- Search area is intentionally static/visual only to satisfy the HTML/CSS-only requirement.
- No push or PR actions performed.
