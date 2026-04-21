# ARCHITECT PLAN — PAP-193

## Ticket
Design a help center homepage using HTML and CSS.

## Objective
Create a clear, accessible support homepage that helps users either:
- find answers quickly through a search-style entry point,
- browse common support categories,
- scan concise FAQ cards,
- or choose a direct contact/support channel.

## Constraints
- HTML and CSS only
- No JavaScript
- Responsive across desktop and mobile
- Prioritize clarity and accessibility

## Current Repository / Stack Observations
From inspection:
- The repo currently uses a single `index.html` entrypoint.
- Styles are embedded inline in a `<style>` block.
- The current page is unrelated to a help center and appears to be a dashboard-style layout.
- The cleanest and lowest-risk approach for this ticket is a full page replacement in `index.html`.

## Recommended Implementation Strategy
Use a **single-page replacement** in `index.html`.

Reasoning:
- The requested help center homepage has a very different information hierarchy from the current page.
- Reusing the current dashboard layout would add noise and increase regression risk.
- A full replacement keeps the structure simpler, easier to review, and more reliable.

## Proposed Page Structure
Build the page in this order:

1. **Hero / help intro**
2. **Search-style support entry area**
3. **Support categories grid**
4. **FAQ cards section**
5. **Contact/support options section**

Recommended semantic structure:
- `<main class="help-page">`
- `<div class="help-shell">`
- `<section class="help-hero">`
- `<section class="categories-panel">`
- `<section class="faq-panel">`
- `<section class="support-panel">`

## Section-by-Section Plan

### 1) Help hero
Purpose:
- immediately tell the user they’re in the support/help center
- reduce friction with a strong heading and short explanatory text

Content recommendation:
- eyebrow or small label like `Support center`
- headline: `How can we help today?`
- short descriptive paragraph
- optional quick-topic chips/links for common intents

Design guidance:
- generous spacing
- high visual hierarchy for heading
- calm, trustworthy tone

### 2) Search-style support entry
Purpose:
- visually communicate that users can search help content

Since JavaScript is not allowed:
- implement a **search-like UI only**, not real search functionality
- use an actual labeled `<input type="search">` for semantics/accessibility
- pair it with a CTA such as `Search guides` or `Browse help`

Requirements:
- explicit visible label
- placeholder text that hints at common searches
- clear focus state for keyboard users
- layout should not break on smaller screens

### 3) Searchable categories section
Purpose:
- let users jump into broad topics if they don’t want to type a search

Suggested categories:
- Account & Login
- Billing & Payments
- Orders & Shipping
- Security & Privacy
- Integrations / Setup
- Technical Issues / Troubleshooting

Each category card should include:
- short label/badge
- category title
- concise description
- small metadata like article count
- CTA text such as `Explore`

Layout guidance:
- 3-column grid on desktop
- 2-column grid on medium screens
- 1-column stack on small mobile

### 4) FAQ cards section
Purpose:
- answer common questions immediately

Suggested FAQ topics:
- password reset
- updating billing details
- tracking orders or requests
- contacting support
- notification preferences
- account access issues

Implementation choice:
- prefer **static FAQ cards** over accordions to keep the HTML/CSS-only solution simple and robust

Each FAQ card should include:
- question as heading
- short answer snippet
- optional `Read more` style link

Layout guidance:
- 2-column grid on desktop/tablet
- 1-column stack on smaller screens

### 5) Contact / support options section
Purpose:
- give users clear escalation paths when self-service isn’t enough

Suggested support options:
- Live chat
- Email support
- Community forum
- Optional phone support if space allows

Each support card should include:
- support channel name
- short explanation of best use case
- response-time or availability note
- CTA such as `Start chat`, `Send email`, or `Open forum`

This section should clearly feel distinct from FAQ content.

## Visual Design Direction
Tone:
- modern
- calm
- readable
- service-oriented

Recommended visual approach:
- light, airy background
- card-based layout with soft borders and subtle shadows
- restrained accent color for buttons, links, and badges
- generous whitespace for scanability
- minimal decoration; content clarity comes first

## Accessibility Requirements
Grunt should include:
- semantic headings and section labels
- visible `:focus-visible` styles for all interactive controls
- labeled search field
- sufficient text/background contrast in both light and dark mode
- readable line length and spacing
- layouts that avoid horizontal scrolling on mobile
- not relying on color alone for meaning

## Dark Mode / Reduced Motion
Include:
- `prefers-color-scheme: dark` styles for visual compatibility
- `prefers-reduced-motion: reduce` fallback to disable nonessential transitions

## Responsive Plan
### Desktop
- hero spans full width
- categories in 3 columns
- FAQ in 2 columns
- support options in 3 columns

### Tablet
- categories/support reduce to 2 columns
- FAQ may remain 2 columns if readable

### Mobile
- search CTA stacks below the search input if needed
- all card grids collapse to 1 column
- spacing remains comfortable and readable

## Reliability / Review Risks
Pedant should specifically inspect:
- whether the search row wraps cleanly below 700px width
- whether all CTA links/buttons remain reachable and legible in dark mode
- whether category/support cards maintain balanced heights with different text lengths
- whether the help page visually reads as a support page rather than a generic marketing page
- whether focus styling is consistently visible on links, chips, and buttons

## Expected File Changes in Grunt Phase
- `index.html`
- optional implementation handoff note file for the next role

## Artifact for Next Role
Grunt should replace the current page with a dedicated help center homepage in `index.html` containing:
- a support hero
- a labeled search-style input area
- category cards
- FAQ cards
- contact/support option cards
- responsive, accessible, light/dark compatible HTML/CSS-only styling
