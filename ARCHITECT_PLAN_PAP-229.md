# ARCHITECT PLAN — PAP-229

## Ticket
Create a pet adoption section using HTML and CSS.

## Scope Summary
Build a friendly adoption-focused section that includes:
- pet cards
- pet image area
- breed information
- age information
- adoption button on each card

Design direction:
- friendly
- warm
- visually inviting

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- this phase is planning only, with no feature implementation

## Current Stack / Structure Observations
Repository snapshot:
- Main frontend entrypoint is `index.html`
- Styling is currently embedded in a single `<style>` block
- The current page is a fitness dashboard layout
- Existing implementation style in this repo favors:
  - single-file HTML/CSS delivery
  - CSS custom properties in `:root`
  - polished section-based layouts
  - responsive grids with card components
  - visible hover/focus states and light/dark support patterns

## High-Level Recommendation
Implement this ticket as a **new themed section within `index.html`**, replacing the current fitness-specific content rather than trying to blend pet adoption cards into dashboard semantics.

Why:
- the current page content is domain-specific to fitness and would create naming/content mismatch
- the requested feature is section-centric and better served by a purpose-built adoption showcase
- a focused pet adoption section can still reuse the repo’s preferred one-file HTML/CSS structure and token-driven styling

## Recommended Section Structure
Use a warm landing-section composition with a strong intro followed by a responsive pet-card grid.

Suggested structure:
- `<main class="adoption-page">`
- `<section class="adoption-section" aria-labelledby="adoption-title">`
- intro/header block
- optional filter/info chips or trust indicators
- pet cards grid
- individual adoption cards with CTA buttons

Suggested class blocks:
- `.adoption-page`
- `.adoption-section`
- `.section-header`
- `.section-eyebrow`
- `.section-copy`
- `.pet-grid`
- `.pet-card`
- `.pet-image`
- `.pet-content`
- `.pet-meta`
- `.pet-badge`
- `.pet-button`

## Information Architecture Plan

### 1) Section intro / emotional framing
The top of the section should immediately communicate warmth and trust.

Recommended contents:
- heading such as “Meet your next best friend”
- short supportive copy about finding loving homes
- one supporting line or chips highlighting adoption benefits such as vaccinated, playful, ready for home

This intro should feel gentle and welcoming, not sales-heavy.

### 2) Pet card grid
The core deliverable is a grid of pet cards.

Each card should include:
- pet image or CSS-styled image placeholder area
- pet name as the primary heading
- breed label
- age label
- short one-line personality description if space allows
- adoption button

Recommended minimum card count:
- 3 cards minimum
- 4 cards preferred for a balanced desktop grid

### 3) Card content hierarchy
Each card should be easy to scan in this order:
1. image
2. pet name
3. breed and age metadata
4. brief descriptive text
5. adoption CTA

Breed and age should be visually grouped so users can compare pets quickly.

### 4) Call-to-action behavior
Buttons do not need JavaScript behavior in this ticket, but they should look actionable and accessible.

Recommended button copy:
- “Adopt Luna”
- “Meet Milo”
- “Start adoption”

CTA styling should:
- feel warm and encouraging
- have clear hover and focus-visible states
- remain readable in light and dark contexts if dark mode is preserved

## Layout Strategy

### Desktop
Recommended arrangement:
- centered intro at top or aligned intro with supporting copy
- 3- or 4-column card grid depending on available width
- equal-height cards for visual rhythm

### Tablet
- shift to 2-column grid
- preserve image prominence
- keep buttons full-width or near full-width for easier tapping

### Mobile
- single-column stack
- generous spacing between cards
- image area remains tall enough to feel inviting
- metadata should wrap cleanly without compressing the CTA

## Visual Style Direction
Target a shelter/adoption aesthetic that feels caring, bright, and approachable.

Recommended design language:
- soft warm neutrals with cheerful accent colors
- rounded cards and generous internal spacing
- subtle shadows for lift without looking corporate
- playful but clean typography hierarchy
- image areas that feel lively, possibly using gradients or soft decorative accents if real images are not embedded

Color direction ideas:
- warm cream / off-white backgrounds
- coral, apricot, golden, sage, or sky accents
- darker cocoa/forest text for contrast

Overall feel should be:
- compassionate
- trustworthy
- joyful
- family-friendly

## Content Recommendations
Use believable adoption-friendly sample content.

Suggested pet data:
- Luna — Golden Retriever — 2 years old
- Milo — Tabby Cat — 1 year old
- Daisy — Beagle Mix — 3 years old
- Coco — Mini Lop Rabbit — 8 months old

Optional supporting descriptions:
- loves cuddle time
- great with kids
- enjoys long walks
- calm indoor companion

## Accessibility / Correctness Requirements
- use semantic heading structure for the section and card titles
- ensure buttons have visible keyboard focus states
- keep text contrast high against soft backgrounds
- do not rely only on the image to communicate breed/age
- maintain meaningful button text
- ensure responsive layout avoids horizontal overflow

## Dark/Light Mode Strategy
If dark mode support is retained, keep it restrained and cozy rather than high-neon.

Recommended approach:
- define section color tokens in `:root`
- use soft light backgrounds by default
- add a `prefers-color-scheme: dark` override if the rest of the page keeps that pattern
- adjust card/background contrast carefully so warm tones stay readable

## Reliability / Regression Risks
Grunt should watch for:
- fitness-specific class names or copy remaining in the final page
- card heights becoming uneven due to inconsistent description length
- image areas collapsing or looking too short on mobile
- adoption buttons wrapping awkwardly on narrow widths
- warm accent colors losing contrast against pale surfaces
- metadata rows becoming cluttered if breed and age are not grouped clearly

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a pet adoption experience rather than a dashboard
- verify each pet card includes image, breed, age, and an adoption button
- verify the section feels warm and visually inviting
- verify the card grid reflows cleanly across desktop, tablet, and mobile
- verify buttons have hover and focus-visible styles
- verify there is no horizontal scrolling
- verify text remains legible in all cards and any supported color schemes

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current fitness-focused content in `index.html` with a responsive pet adoption section featuring a welcoming section intro and a grid of adoption cards. Each card should include a prominent image area, pet name, breed, age, optional short personality copy, and a clear adoption button, all implemented with HTML and CSS only.
