# ARCHITECT PLAN — PAP-187

## Ticket
Create a movie streaming homepage using HTML and CSS.

## Scope Summary
Design a homepage that includes:
- a featured movie banner
- category sections
- responsive movie cards
- an overall feel similar to a streaming platform

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- polished, cinematic, platform-like presentation

## Current Stack / Structure Observations
Repository snapshot:
- Primary frontend file: `index.html`
- Styles are inline inside the page `<style>` block
- The current page is a restaurant menu layout, so this ticket is best treated as another single-page replacement
- Existing code patterns already support:
  - tokenized colors and spacing
  - rounded surfaces/cards
  - responsive breakpoints
  - dark mode

## High-Level Recommendation
Treat this ticket as a **standalone homepage replacement** in `index.html`.

Why:
- a streaming homepage has a very distinct layout language
- it needs a cinematic hero and content rails/cards that differ from the current restaurant structure
- replacing the existing page will produce a cleaner result than trying to embed streaming sections into the current markup

## Implementation Direction

### 1) Replace the current body content with a dedicated streaming homepage
Grunt should convert `index.html` into a streaming-style landing/home page.

Recommended structure:
- `<main class="streaming-page">`
- featured hero banner at top
- stacked category sections below
- each category contains a responsive movie card grid or horizontally styled rail-like card layout built with CSS grid

Suggested major blocks:
- `.streaming-page`
- `.streaming-shell`
- `.featured-banner`
- `.featured-copy`
- `.featured-actions`
- `.category-section`
- `.section-header`
- `.movie-grid`
- `.movie-card`
- `.movie-poster`
- `.movie-meta`

### 2) Featured banner plan
The top section should feel cinematic and high-priority.

Recommended banner contents:
- eyebrow or platform label
- featured title
- short plot-style summary
- optional metadata row (genre, runtime, rating)
- primary CTA button such as `Watch now`
- secondary CTA like `Add to list` or `View details`

Visual direction:
- dark, moody, poster-like background using gradients or CSS-only artwork
- strong contrast between text and background
- layered overlay so text remains readable

### 3) Category sections plan
Add multiple sections that resemble streaming homepage rows.

Example categories:
- Trending Now
- New Releases
- Action & Adventure
- Continue Watching or Editor's Picks

Each section should include:
- section heading
- optional short subtitle or tag
- responsive grid of movie cards

### 4) Movie card plan
Each movie card should include:
- poster/thumbnail area
- movie title
- short genre or metadata line
- optional small badge (Top Pick, New, 4K, etc.)

Card design guidance:
- posters should feel tall and cinematic, even if they are CSS-only placeholders
- hover should slightly elevate or brighten cards without becoming noisy
- typography should prioritize title clarity and easy scanning

Recommended card structure:
- poster block on top
- title below
- supporting metadata below
- optional badge aligned above or within the poster area

### 5) Layout and responsiveness
Desktop:
- large hero banner at top
- categories beneath in 4-column or auto-fit card grids depending on width

Tablet:
- hero can stack or tighten spacing
- movie grids reduce to fewer columns gracefully

Mobile:
- hero becomes single-column and more compact
- movie cards stack in 1–2 columns depending on chosen min width
- CTA buttons in the hero should remain easy to tap

### 6) Visual style direction
Aim for a premium streaming aesthetic:
- dark-forward palette
- strong accent color for primary actions
- glossy or cinematic poster placeholders
- soft glows/shadows, but restrained
- clear separation between hero and content rails

Recommended color tone:
- deep charcoal/navy background
- cool highlight or bold red/blue accent depending on taste
- keep text high-contrast and legible

### 7) Accessibility / Correctness Requirements
- semantic headings for homepage and category titles
- interactive elements must have visible `:focus-visible` states
- maintain sufficient contrast over dark backgrounds and poster cards
- preserve logical reading order when the layout collapses on mobile
- if poster visuals are decorative, use appropriate `aria-hidden` handling where needed

### 8) Dark Mode Strategy
Because streaming interfaces are usually dark-forward, the page can intentionally lean into a dark presentation.

Recommended approach:
- design primarily around a dark theme
- if light mode is preserved, ensure it remains usable, but dark mode should be the priority aesthetic
- avoid low-contrast muted text on already-dark poster surfaces

## Suggested Content Structure
Featured movie:
- one hero title with a short cinematic summary
- 2 CTA buttons

Category groups:
- Trending Now
- New Releases
- Sci-Fi Picks
- Award Winners

Each category should contain 4–6 cards, enough to feel like a real streaming homepage without overcrowding the page.

## Regression / Reliability Risks
Since this is likely a page replacement, Grunt should watch for:
- leftover restaurant-specific styles affecting spacing or colors
- hero text becoming unreadable against decorative gradients
- inconsistent movie card heights due to varying title lengths
- mobile card columns becoming too narrow for readable metadata
- hover effects feeling too aggressive on touch-sized layouts

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a movie streaming homepage
- verify the featured banner, category sections, and responsive movie cards are all present
- verify hero CTA buttons have clear hover/focus states
- verify card grid remains balanced across desktop, tablet, and mobile
- verify no horizontal overflow occurs
- verify the overall feel is cinematic and platform-like
- verify text remains readable over dark surfaces and poster placeholders

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should implement the streaming homepage directly in `index.html`, likely replacing the current restaurant menu page with a dedicated featured-banner plus multi-section movie card layout and updating the inline CSS to match the streaming aesthetic.
