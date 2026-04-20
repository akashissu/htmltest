# ARCHITECT PLAN — PAP-190

## Ticket
Build a real estate property listing section using HTML and CSS.

## Scope Summary
Create a polished, professional property showcase that includes:
- house images
- prices
- location
- feature details such as bedrooms and bathrooms

Design direction:
- polished
- professional
- listing/showcase focused

Constraints:
- HTML + CSS only
- responsive across desktop and mobile
- no JavaScript required

## Current Stack / Structure Observations
Repository snapshot:
- Main entrypoint is `index.html`
- Styles are embedded in an inline `<style>` block
- The current page is a fitness dashboard layout
- Existing repo pattern suggests one-file page replacements for each task rather than incremental multi-file builds

## High-Level Recommendation
Treat this ticket as a **single-page replacement in `index.html`** built around a dedicated real estate listing section.

Why:
- the current fitness dashboard is structurally unrelated
- real estate listings benefit from a different visual hierarchy centered on media cards and property metadata
- replacement will be cleaner than trying to retrofit the existing dashboard card system

## Recommended Output Shape
Implement a real estate showcase page or section that feels like a professional property browsing experience.

Suggested structure:
- `<main class="property-page">`
- `<div class="property-shell">`
- hero/intro block for browsing properties
- property listing grid with multiple property cards
- optional filter-style summary chips or market stats row

Suggested class blocks:
- `.property-page`
- `.property-shell`
- `.property-hero`
- `.hero-copy`
- `.hero-visual`
- `.market-highlights`
- `.highlight-card`
- `.property-grid`
- `.property-card`
- `.property-image`
- `.property-content`
- `.property-price`
- `.property-location`
- `.property-features`
- `.feature-pill`

## Information Architecture Plan

### 1) Intro / hero area
Top section should establish a premium real-estate tone.

Recommended contents:
- headline about finding a home or featured listings
- short supporting description
- optional CTA like `View listings` or `Schedule a tour`
- optional summary chips such as `Luxury`, `Family Homes`, `City Living`
- decorative property-themed visual using CSS only if no real images are available

This area should feel calm, upscale, and editorial.

### 2) Listing section
Main section should be a grid of property cards.

Each property card should include:
- large visual/image area at top
- price
- property title or neighborhood label
- location line
- feature row with bedroom/bathroom/square-foot details
- optional badge like `New Listing`, `Open House`, or `Featured`

Recommended number of cards:
- 4 to 6 cards

That is enough to feel like a real listing section without overcrowding the page.

### 3) Property image strategy
Since the task requests house images and tools are HTML/CSS only, Grunt should choose one of these paths:

Preferred:
- use CSS-crafted property image placeholders that resemble architectural/photo cards

Alternative if appropriate and already available locally:
- use simple static image references only if safe and available in the repo

Important:
- if images are decorative placeholders, make them polished enough to still read as premium property media
- maintain consistent image aspect ratio across all cards

### 4) Property metadata presentation
Recommended layout inside each card:
- badge near image or above title
- price prominently displayed
- short title or area/neighborhood name
- location line below
- features row below using compact pills or evenly spaced metadata items

Suggested metadata examples:
- 4 Beds
- 3 Baths
- 2,450 sq ft

Potential additional metadata:
- garage
- garden
- waterfront
- penthouse

### 5) Supporting highlights row (optional but recommended)
To make the section feel more complete and polished, include a small row of highlight cards above the property grid.

Examples:
- Curated premium listings
- Verified agents
- Flexible viewing slots

These should remain secondary to the actual property cards.

## Layout Strategy

### Desktop
- large intro/hero block at top
- property grid beneath in 3 columns or auto-fit layout depending on card width
- highlight row can appear between hero and listings if used

### Tablet
- property cards reduce to 2 columns
- hero may stack if visual and copy become cramped

### Mobile
- single-column property cards
- prices and features remain clearly readable
- location and detail rows should wrap gracefully without overflow

## Visual Style Direction
Aim for a professional real-estate aesthetic.

Recommended design language:
- neutral premium palette: navy, slate, charcoal, stone, warm beige, or muted gold accents
- crisp typography with clear hierarchy
- restrained shadows and clean card edges
- elevated but not flashy visual treatment
- slightly editorial / luxury brochure feel

Overall feel should be:
- trustworthy
- polished
- premium
- organized

## Accessibility / Correctness Requirements
- semantic headings for hero and listing section
- visible `:focus-visible` styles for buttons/links
- property details must remain readable at mobile widths
- avoid relying only on badges or color to communicate status
- decorative images/placeholders should use `aria-hidden` when appropriate

## Dark/Light Mode Strategy
Recommended approach:
- prioritize a bright, professional default theme
- preserve dark-mode compatibility if practical using `prefers-color-scheme: dark`
- ensure prices and metadata retain strong contrast in both themes

## Suggested Content Plan

### Hero
- title focused on discovering or browsing exceptional homes
- short descriptive copy
- 1–2 CTAs or browsing links

### Property cards
Include 4–6 cards such as:
- modern hillside home
- urban penthouse
- family house in a quiet neighborhood
- waterfront villa

Each with:
- price
- location
- 3 metadata points minimum

## Reliability / Regression Risks
Grunt should watch for:
- leftover fitness-dashboard styles leaking into the new layout
- inconsistent card heights due to different title/location lengths
- feature metadata wrapping awkwardly on narrow widths
- property image areas not maintaining consistent aspect ratio
- prices or badges lacking enough contrast over image backgrounds
- overly decorative visuals making the layout feel less professional

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a real estate property showcase
- verify house imagery/visual placeholders, prices, locations, and feature details are all present
- verify property cards align cleanly across desktop, tablet, and mobile
- verify no horizontal overflow occurs
- verify badges, prices, and feature metadata remain readable
- verify the overall design feels polished and professional
- verify light and dark modes both remain coherent

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current page in `index.html` with a professional real estate listing experience featuring a hero/intro area and a responsive grid of property cards containing visual media, pricing, location, and property features.
