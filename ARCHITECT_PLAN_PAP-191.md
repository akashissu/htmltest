# ARCHITECT PLAN — PAP-191

## Ticket
Create a social media profile page using HTML and CSS.

## Scope Summary
Design a profile page with:
- cover image
- profile card
- stats
- post grid

Design direction:
- modern
- balanced
- profile-centric

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- no JavaScript required

## Current Stack / Structure Observations
Repository snapshot:
- Main frontend entrypoint is `index.html`
- Styling is embedded in an inline `<style>` block
- The current page is a fitness dashboard layout
- Existing repo pattern favors single-page replacements rather than partial integration into older layouts

## High-Level Recommendation
Treat this ticket as a **full single-page replacement in `index.html`**.

Why:
- a social profile page needs a distinct visual hierarchy centered around identity and content
- current fitness-dashboard semantics and components are not reusable without creating unnecessary complexity
- a clean replacement will better support the requested cover image, profile card, stats, and post grid

## Recommended Page Structure
Implement a profile-style layout that feels like a modern social media page.

Suggested structure:
- `<main class="profile-page">`
- `<div class="profile-shell">`
- cover/hero section at top
- profile summary card overlapping or visually connected to the cover
- stats row or stat cards
- content area with post grid

Suggested class blocks:
- `.profile-page`
- `.profile-shell`
- `.cover-banner`
- `.cover-visual`
- `.profile-card`
- `.avatar`
- `.profile-meta`
- `.profile-actions`
- `.stats-grid`
- `.stat-card`
- `.posts-panel`
- `.post-grid`
- `.post-card`
- `.post-media`
- `.post-meta`

## Information Architecture Plan

### 1) Cover / hero area
Top section should establish the visual identity of the page.

Recommended contents:
- wide cover image area or CSS-crafted cover visual
- optional subtle overlay for text readability
- profile card visually anchored near or overlapping the cover area

The cover should make the page feel social and visually engaging without overwhelming the rest of the content.

### 2) Profile card
Primary identity block should include:
- avatar/profile image area
- display name
- handle or short subtitle
- short bio
- action buttons such as `Follow` and `Message` or equivalent

Optional supporting metadata:
- location
- website
- creative role / tagline

This card should feel modern and clean, with clear hierarchy between name, handle, and bio.

### 3) Stats section
Add a concise stats area to make it feel like a real profile page.

Suggested stats:
- posts
- followers
- following
- likes or saves

Presentation guidance:
- 3–4 equally weighted stat cards or a horizontal stat row
- large values with smaller labels
- keep it simple and scannable

### 4) Post grid section
Main content area should be a responsive post grid.

Recommended grid contents:
- 6 to 9 post cards
- each card includes a visual/media block plus minimal supporting metadata

Possible metadata:
- caption snippet
- date or category tag
- likes/comments counts

Since no JavaScript is allowed, this should remain a static showcase grid, but still feel like a social feed/profile gallery.

### 5) Media / image strategy
The ticket asks for a cover image and a post grid. With HTML/CSS only, Grunt should use:

Preferred:
- CSS-crafted visuals/placeholders for cover, avatar, and posts

Alternative:
- local image assets only if they already exist and are safe to reference

Requirements:
- maintain consistent aspect ratios across post cards
- ensure the cover visual feels distinct from post thumbnails
- keep the avatar/profile image visually separate and prominent

## Layout Strategy

### Desktop
Recommended arrangement:
- cover spans full width within the page shell
- profile card sits directly below or partially overlaps the cover
- stats row below profile summary
- post grid below in 3-column or auto-fit layout

### Tablet
- profile summary can stack more vertically
- stats grid reduces columns cleanly
- post grid can reduce to 2 columns

### Mobile
- cover remains visible but becomes more compact
- profile card stacks naturally
- stats become 2-column or 1-column as needed
- post grid should likely become 1–2 columns depending on minimum width

## Visual Style Direction
Aim for a modern, balanced social platform aesthetic.

Recommended design language:
- clean neutral background with one or two vibrant accents
- rounded cards and subtle shadows
- airy spacing
- balanced typography hierarchy
- polished but lightweight visual treatment

Overall feel should be:
- contemporary
- personable
- polished
- content-forward

## Accessibility / Correctness Requirements
- semantic headings for major page sections
- visible `:focus-visible` styles on interactive elements
- maintain readable contrast over cover/post visuals
- ensure bio, stats, and captions remain readable at narrow widths
- decorative image placeholders should use `aria-hidden` where appropriate

## Dark/Light Mode Strategy
Recommended approach:
- support both light and dark via CSS tokens
- default can be bright and modern
- dark mode should preserve readable text over media placeholders and surfaces

## Suggested Content Plan

### Profile identity
- display name
- handle
- short creative/professional bio
- 2 action buttons

### Stats
- Posts
- Followers
- Following
- Likes

### Post grid
Include 6–9 cards with varied but consistent captions/tags, such as:
- travel/lifestyle card
- design/workspace card
- portrait/creative card
- city/night card
- minimal food/coffee card
- moodboard/nature card

## Reliability / Regression Risks
Grunt should watch for:
- leftover fitness-dashboard styles leaking into the new layout
- overlap between cover and profile card breaking on smaller screens
- stats row becoming cramped or wrapping awkwardly on tablets
- post grid captions causing uneven card heights in an ugly way
- insufficient contrast when text sits over decorative cover/post backgrounds
- excessive decoration causing the layout to feel noisy rather than balanced

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a social media profile page
- verify cover image area, profile card, stats, and post grid are all present
- verify profile hierarchy is clear: avatar, name, handle, bio, actions
- verify post grid remains balanced across desktop, tablet, and mobile
- verify no horizontal overflow occurs
- verify interactive elements have visible focus states
- verify the overall visual feel is modern and balanced

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current page in `index.html` with a modern social media profile layout featuring a cover banner, profile card, stats section, and responsive post grid, all implemented with HTML and CSS only.
