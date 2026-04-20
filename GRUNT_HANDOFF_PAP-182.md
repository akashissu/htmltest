# PAP-182 — Grunt handoff for Pedant

## What I changed
- Added a new countdown / launch banner section to `index.html`.
- Placed it in `.workspace-main` directly below the dashboard section and above testimonials, matching the architect recommendation.
- Implemented the section using HTML and CSS only.
- Added:
  - eyebrow label
  - launch heading
  - short launch message
  - four countdown blocks for days, hours, minutes, and seconds
  - primary CTA button linking to `#docs`
- Added section-specific CSS inside the existing inline `<style>` block.
- Extended the current responsive breakpoints so the banner stacks cleanly at tablet widths and the countdown shifts to two columns on small screens.
- Reused the existing theme tokens and interaction language so the section works in light and dark mode without new theme plumbing.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-182.md`

## What Pedant should verify
- The launch banner appears between dashboard and testimonials.
- Countdown grid renders as 4 columns on wider screens and 2 columns on narrow screens.
- No horizontal overflow appears on mobile widths.
- CTA button hover and focus-visible states are clear and consistent with the existing page.
- Section remains visually balanced in both light and dark mode.
- Decorative gradient background does not reduce text contrast.
- Existing sections were not visually regressed by the new styles.

## Notes
- Countdown values are static by design because the ticket requires HTML and CSS only.
- No JavaScript added.
- No push or PR actions performed.
