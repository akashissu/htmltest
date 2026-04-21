# ARCHITECT PLAN — PAP-192

## Ticket
Design a help center homepage using HTML and CSS.

## Scope Summary
Build a support/help page with:
- searchable categories
- FAQ cards
- contact/support options

Design direction:
- clear
- accessible
- support-oriented

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- no JavaScript required

## Current Stack / Structure Observations
Repository snapshot:
- Main frontend entrypoint is `index.html`
- Styling is embedded inside an inline `<style>` block
- The current page is a non-help-center layout
- Existing repo pattern suggests page-level replacements are the cleanest approach for these tickets

## High-Level Recommendation
Treat this ticket as a **full single-page replacement in `index.html`**.

Why:
- a help center homepage has a distinct content hierarchy focused on guidance and support
- current page semantics are unrelated and would create unnecessary carryover risk
- replacing the page allows a cleaner structure for search, categories, FAQs, and contact options

## Recommended Page Structure
Implement a support homepage that feels easy to scan and reassuring to use.

Suggested structure:
- `<main class="help-page">`
- `<div class="help-shell">`
- hero / support intro section with search-style input UI
- category section
- FAQ card section
- contact / support options section

Suggested class blocks:
- `.help-page`
- `.help-shell`
- `.help-hero`
- `.hero-copy`
- `.search-panel`
- `.search-field`
- `.categories-panel`
- `.category-grid`
- `.category-card`
- `.faq-panel`
- `.faq-grid`
- `.faq-card`
- `.support-panel`
- `.support-grid`
- `.support-card`

## Information Architecture Plan

### 1) Hero / intro section
Top section should quickly orient users and reduce friction.

Recommended contents:
- clear heading such as “How can we help?”
- brief supporting text
- search-style field UI (visual only, since no JS)
- optional quick links/tags for common help topics

Important note:
- because the page is HTML/CSS only, the search should be presented as a **search-like interface** rather than functional search logic
- ensure the search input/button visually reads as accessible and obvious

### 2) Searchable categories section
Add a prominent category area users can browse if search isn’t enough.

Suggested categories:
- Account & Login
- Billing & Payments
- Orders / Shipping
- Security & Privacy
- Integrations / Setup
- Troubleshooting

Each category card should include:
- category title
- short supporting description
- optional article count or label

This section should feel easy to scan and not overly dense.

### 3) FAQ section
Add a set of FAQ cards for common questions.

Suggested FAQ content:
- password reset
- updating billing details
- tracking an order/request
- contacting support
- changing notification settings
- troubleshooting account access

Presentation guidance:
- use compact cards rather than long accordion patterns
- each card should include:
  - question title
  - short answer snippet
  - optional `Read more` style link

Since no JavaScript is allowed, avoid dynamic accordion behavior unless done via pure HTML/CSS and it remains accessible. Safer option: static FAQ cards.

### 4) Contact / support options section
Include direct support paths near the bottom.

Suggested options:
- Live chat
- Email support
- Call support
- Community/help forum

Each support card should include:
- label/title
- short description
- availability or response time
- CTA link/button

This section should reassure users that there is a next step if self-service doesn’t solve the problem.

## Layout Strategy

### Desktop
Recommended arrangement:
- hero at top with search emphasis
- categories in 2–3 columns beneath
- FAQ grid below
- support options in a final row/grid

### Tablet
- categories reduce to 2 columns
- FAQ cards and support cards remain comfortably spaced
- hero search stays prominent and full width

### Mobile
- everything stacks vertically
- search input/button remain easy to tap
- category, FAQ, and support cards collapse to single-column layout
- text remains readable with generous spacing

## Visual Style Direction
Aim for a professional, approachable help center aesthetic.

Recommended design language:
- bright, neutral base colors
- one calm accent color for emphasis
- clear card separation and hierarchy
- restrained shadows
- accessible typography with generous spacing

Overall feel should be:
- trustworthy
- supportive
- easy to navigate
- calm and uncluttered

## Accessibility / Correctness Requirements
- semantic headings for each major section
- visible `:focus-visible` states for links and buttons
- search input should include proper label or accessible naming
- maintain strong color contrast for text and CTAs
- avoid relying only on color to distinguish categories or support urgency
- ensure layouts do not overflow on smaller screens

## Dark/Light Mode Strategy
Recommended approach:
- default to a bright, clear help-center presentation
- provide dark-mode compatibility via `prefers-color-scheme: dark`
- ensure form-like search UI and card content remain clearly separated in both themes

## Suggested Content Plan

### Hero
- title: “How can we help today?”
- short support-oriented subtitle
- search field + button
- quick links/tags for common tasks

### Categories
- 6 cards covering common support areas

### FAQs
- 4–6 FAQ cards with concise answers

### Support options
- 3–4 support method cards with availability info

## Reliability / Regression Risks
Grunt should watch for:
- leftover old-page styles leaking into the help-center layout
- search field/button wrapping awkwardly on small screens
- category cards becoming uneven due to copy length differences
- FAQ cards becoming too text-heavy and harming scanability
- contact options not visually distinct enough from FAQ cards
- insufficient focus styling on interactive elements

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a help center homepage
- verify search UI, categories, FAQ cards, and support options are all present
- verify the search area is prominent and understandable even if static
- verify category and FAQ cards remain balanced across desktop, tablet, and mobile
- verify no horizontal overflow occurs
- verify interactive elements have visible focus states
- verify the page feels clear, accessible, and easy to scan

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current page in `index.html` with a clear, accessible help center homepage featuring a hero/search area, searchable category cards, FAQ cards, and contact/support options, all implemented with HTML and CSS only.
