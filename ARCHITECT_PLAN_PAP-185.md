# ARCHITECT PLAN — PAP-185

## Ticket
Design a travel destination landing page using HTML and CSS.

## Scope Summary
Build a bright, welcoming landing page that includes:
- a hero banner
- destination cards
- short travel descriptions
- a booking button

Constraints:
- HTML + CSS only
- visually inviting and modern
- responsive across desktop and mobile

## Current Stack / Structure Observations
Repository snapshot:
- Primary frontend file: `index.html`
- Styling is inline inside the page `<style>` block
- The current page uses a general-purpose landing/dashboard style with:
  - tokenized colors and spacing in `:root`
  - rounded card/panel surfaces
  - responsive breakpoints
  - dark mode support

## High-Level Recommendation
Treat this ticket as a **standalone landing page replacement** in `index.html`.

Why:
- the requested UI is a full landing page concept, not a small additive component
- the page needs a cohesive travel-specific mood and structure
- replacing the current demo page is cleaner than trying to insert travel content into the existing layout shell

## Implementation Direction

### 1) Replace the current body content with a dedicated travel landing page
Grunt should convert `index.html` into a travel-focused landing page.

Recommended structure:
- `<main class="travel-page">`
- hero section with headline, short supporting copy, and booking CTA
- destinations section with multiple destination cards
- optional small trust/stat strip if needed for visual rhythm

Suggested major blocks:
- `.travel-page`
- `.travel-shell`
- `.hero`
- `.hero-copy`
- `.hero-visual`
- `.booking-button`
- `.destinations-section`
- `.destinations-grid`
- `.destination-card`
- `.destination-card__image`
- `.destination-card__body`

### 2) Hero section plan
The hero should establish the bright, welcoming tone immediately.

Recommended hero content:
- small eyebrow label like `Explore the world` or `Summer escapes`
- strong headline focused on discovery/travel
- short paragraph describing curated destinations or memorable getaways
- primary booking button
- optional secondary supporting chip/stat line if it helps balance the layout

Hero visual recommendation:
- use CSS gradients or inline SVG/data URI artwork instead of external assets
- create a bright, airy travel feel with sky/ocean/sunrise inspired tones

### 3) Destination cards plan
Add a destination grid beneath the hero.

Each card should include:
- destination name
- short description
- optional small metadata (e.g. region, duration, “best for”) if helpful
- clear visual hierarchy

Recommended destination count:
- 3 to 6 cards

Card structure suggestion:
- top image/illustration area
- title
- short descriptive text
- optional mini footer/tag row

### 4) CTA behavior
Include at least one prominent booking button, preferably in the hero.

Optional:
- small CTA/button on each destination card such as `View trip` or `See details`
- but if the page starts to feel too busy, keep the main CTA only in the hero

Recommended default:
- one primary hero booking button
- optional lightweight destination card links only if the layout still feels clean

### 5) Visual style direction
Aim for:
- bright, warm, welcoming palette
- spacious layout
- soft shadows and rounded cards
- strong but not heavy typography
- colorful destination illustrations or gradient image placeholders

Suggested visual language:
- whites, soft sky blues, sand/coral accents, maybe a teal accent for freshness
- avoid overcomplicating the page with too many decorative layers
- prioritize clarity and aspiration

### 6) Responsive behavior
Desktop:
- hero may use a two-column layout with copy + visual
- destination cards can use a 3-column or auto-fit grid

Tablet:
- hero should stack if needed
- destination grid should reduce columns gracefully

Mobile:
- single-column hero layout
- destination cards stack cleanly
- booking button remains obvious and easy to tap
- avoid text blocks becoming too wide or cramped

### 7) Accessibility / Correctness Requirements
- semantic headings for hero and section titles
- strong color contrast for headings, descriptions, and CTA button
- visible hover and `:focus-visible` states for interactive elements
- logical reading order when the hero stacks on mobile
- if destination images are decorative, use appropriate alt handling

### 8) Dark Mode Strategy
The current project supports dark mode, so Grunt should preserve it if practical.

Recommended approach:
- keep light mode as the primary visual target since the brief emphasizes bright and welcoming
- still provide a clean dark mode adaptation by reusing tokenized colors where possible
- ensure bright travel tones do not become neon or muddy in dark mode

## Suggested Content Structure
Example hero copy:
- Eyebrow: `Explore beyond the ordinary`
- Headline: `Find your next unforgettable getaway`
- Supporting text: one sentence about curated destinations and easy trip planning
- CTA: `Book your escape`

Example destinations:
- Santorini, Greece
- Kyoto, Japan
- Bali, Indonesia
- Amalfi Coast, Italy

## Regression / Reliability Risks
Because this is likely a page replacement, Grunt should watch for:
- leftover layout classes or scripts from the current page affecting spacing
- hero visuals overwhelming text readability
- card grid becoming uneven with longer destination descriptions
- CTA styling feeling disconnected from the rest of the page
- mobile layout crowding the hero or destination cards

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a travel landing page
- verify hero, destination cards, short descriptions, and booking button are all present
- verify the layout feels bright and welcoming in light mode
- verify the page remains usable and readable in dark mode if preserved
- verify hover/focus states on the booking button and any card actions
- verify no horizontal overflow on smaller screens
- verify destination cards remain easy to scan on mobile

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should implement the travel landing page directly in `index.html`, likely replacing the current page with a dedicated hero + destination card layout and updating the inline CSS to support the new design.
