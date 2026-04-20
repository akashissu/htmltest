# ARCHITECT PLAN — PAP-182

## Ticket
Add a responsive countdown / launch banner section using HTML and CSS.

## Scope Summary
Create a new frontend section that includes:
- a heading
- a short launch message
- countdown blocks for:
  - days
  - hours
  - minutes
  - seconds
- a call-to-action button

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- visually polished
- consistent with the existing page design
- support dark mode if already present

## Current Stack / Structure Observations
Repository snapshot:
- Primary frontend file: `index.html`
- Styles live inside the inline `<style>` block in `index.html`
- The page already uses:
  - design tokens in `:root`
  - reusable panel styling via `.workspace-panel`
  - responsive breakpoints at `900px` and `640px`
  - dark mode via `@media (prefers-color-scheme: dark)`
  - consistent hover/focus treatment for buttons and cards

Current layout landmarks in `.workspace-main`:
- `#search-panel`
- `#dashboard`
- `#testimonials`
- `#blog`

Sidebar sections:
- `#docs`
- `#settings`

## Placement Recommendation
Add the countdown / launch banner as a new `<section class="workspace-panel">` inside `.workspace-main`, ideally **between the dashboard and testimonials sections**.

Why this placement works:
- the banner reads as a high-priority promotional/status block
- it fits naturally after metrics/dashboard content
- it keeps the launch CTA prominent before longer testimonial/blog content
- it does not overload the narrower sidebar

Alternative acceptable placement:
- directly below the blog section if the Grunt wants to minimize disturbance to the current reading flow

Preferred default: **below dashboard, above testimonials**.

## Implementation Plan

### 1) Add new section markup in `index.html`
Create a section with an id such as:
- `id="launch-banner"`

Recommended structure:
- `.workspace-panel.launch-banner`
- inner wrapper: `.launch-banner__layout`
- copy/content area: `.launch-banner__copy`
- countdown grid: `.launch-banner__countdown`
- countdown item blocks: `.countdown-block`
- CTA area: `.launch-banner__actions`

Recommended content hierarchy:
- eyebrow: `Launching Soon` or `Launch Countdown`
- heading: short launch-focused headline
- supporting paragraph: concise message explaining the launch
- CTA button: e.g. `Get notified`, `Join the waitlist`, or `See launch details`
- countdown blocks with static values for:
  - days
  - hours
  - minutes
  - seconds

Important note:
- Because the ticket explicitly requires HTML and CSS only, the countdown must be **static visual content**, not a live updating timer.
- Grunt should present it as a polished launch countdown display, using fixed numbers.

### 2) Add section-specific CSS in the existing `<style>` block
Place the new styles near other section/card styles so the page stays maintainable.

Recommended CSS responsibilities:
- define a banner layout that feels more promotional than a standard text panel
- create a countdown grid using equal-height blocks/cards
- allow CTA alignment to feel balanced with the timer on desktop and stacked on mobile
- reuse current tokens for borders, shadows, radius, accent, and text colors

Recommended class set:
- `.launch-banner`
- `.launch-banner__layout`
- `.launch-banner__copy`
- `.launch-banner__countdown`
- `.countdown-block`
- `.countdown-block strong`
- `.countdown-block span`
- `.launch-banner__actions`
- `.launch-banner__button`

Styling direction:
- use a subtle gradient or accent-tinted background that still fits the existing aesthetic
- keep borders and shadows aligned with `.workspace-panel` and existing button language
- ensure numbers feel visually prominent with strong typographic hierarchy
- give the CTA button the same interaction quality as the current primary actions

### 3) Responsive behavior
At desktop widths:
- allow the copy and CTA to sit alongside or above the countdown depending on the chosen composition
- countdown blocks should appear in a 4-column grid when space allows

At `max-width: 900px`:
- stack banner content more vertically if needed
- keep countdown grid readable and centered/aligned without awkward spacing

At `max-width: 640px`:
- reduce padding where appropriate
- allow countdown blocks to shift to 2 columns if 4 columns becomes cramped
- CTA button should become full width or comfortably wrap
- avoid horizontal overflow from large number sizing or fixed-width blocks

## Dark Mode Strategy
Reuse current theme variables instead of inventing a second palette.

Use existing tokens where possible:
- `--card-bg`
- `--section-bg`
- `--text-primary`
- `--text-secondary`
- `--accent`
- `--accent-soft`
- `--border`
- `--shadow`
- `--shadow-hover`

If decorative gradients are added:
- keep them subtle
- ensure number blocks still have clear contrast in dark mode
- avoid washed-out low-contrast text against tinted backgrounds

## Accessibility / Correctness Requirements
- section should use `aria-labelledby` tied to the main heading
- CTA must remain keyboard accessible
- CTA needs visible `:focus-visible` treatment
- countdown labels should be text, not background images
- number blocks should preserve readable contrast in both light and dark mode
- static countdown values are acceptable, but the markup should still read clearly and logically

## Regression Risks to Watch
- countdown blocks becoming too narrow on mobile
- large digits causing overflow or uneven card heights
- CTA button crowding the timer grid on tablet widths
- decorative background overpowering existing page styling
- dark mode contrast loss in accent-tinted timer blocks

## Suggested QA Checklist for Pedant
- verify the launch banner appears in the intended position in `.workspace-main`
- verify the section includes heading, launch message, CTA, and all four countdown blocks
- verify countdown blocks remain balanced at desktop, tablet, and mobile widths
- verify there is no horizontal scrolling on common mobile widths
- verify CTA hover/focus states are clear and consistent with the page
- verify the section remains visually integrated with the rest of the interface
- verify contrast/readability in dark mode

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should implement the countdown / launch banner directly in `index.html`, adding both:
- the new section markup in `.workspace-main`
- the required inline CSS in the existing `<style>` block

The implementation should remain HTML/CSS only, with a static countdown presentation rather than a live timer.
