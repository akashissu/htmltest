# ARCHITECT PLAN — PAP-189

## Ticket
Design a fitness app dashboard using HTML and CSS.

## Scope Summary
Build a dashboard showing:
- workout stats
- progress cards
- daily goals
- schedule sections

Design direction:
- energetic
- clean
- dashboard-oriented

Constraints:
- HTML + CSS only
- responsive on desktop and mobile
- no JavaScript required

## Current Stack / Structure Observations
Repository snapshot:
- Main frontend entrypoint is `index.html`
- Styling is currently inline inside a `<style>` block
- The current page is a restaurant-style landing/menu page
- Existing implementation style in this repo favors:
  - one-file HTML/CSS replacements
  - design tokens in `:root`
  - section-based responsive layouts
  - light/dark mode support via CSS

## High-Level Recommendation
Implement this ticket as a **full single-page dashboard replacement** in `index.html`.

Why:
- A fitness dashboard has a very different structure from a marketing page or menu page
- It benefits from a card-based information hierarchy
- Replacing the current page is cleaner and reduces the risk of carrying over unrelated styling semantics

## Recommended Page Structure
Use a dashboard-style layout with one strong overview area followed by supporting info cards.

Suggested structure:
- `<main class="fitness-page">`
- `<div class="fitness-shell">`
- hero/overview summary card at top
- compact stats grid
- progress cards section
- daily goals section
- schedule/workout plan section

Suggested class blocks:
- `.fitness-page`
- `.fitness-shell`
- `.dashboard-hero`
- `.hero-copy`
- `.hero-visual`
- `.stats-grid`
- `.stat-card`
- `.progress-grid`
- `.progress-card`
- `.goals-panel`
- `.goal-list`
- `.goal-item`
- `.schedule-panel`
- `.schedule-list`
- `.schedule-item`

## Information Architecture Plan

### 1) Top dashboard overview
The top section should immediately communicate that this is a fitness app dashboard.

Recommended contents:
- heading such as “Train smarter this week” or similar
- short supporting copy
- a compact set of headline metrics
- optional CTA or filter-style pills (e.g. Weekly Plan / Recovery / Nutrition)
- decorative fitness-themed visual built with CSS only

This section should feel energetic but still clean and structured.

### 2) Workout stats section
Include a stat grid with 3–4 concise cards.

Suggested stats:
- workouts completed
- calories burned
- active minutes
- recovery score or streak

Card guidance:
- large number/value
- small supporting label
- optional trend indicator or caption
- equal-height presentation for visual stability

### 3) Progress cards section
This should visualize ongoing fitness progress using CSS-only styling.

Suggested card ideas:
- weekly activity progress
- strength progress
- hydration or recovery progress
- step goal completion

Since no JavaScript is allowed, use visual progress representations via:
- progress bars
- segmented fills
- circular-like decorative blocks if simple enough in CSS

Keep the progress cards legible and not overly decorative.

### 4) Daily goals section
Add a dedicated card or panel for daily goals.

Suggested goals:
- steps
- water intake
- sleep target
- protein target

Recommended presentation:
- list of goal rows
- each row includes label, status/value, and a simple progress indicator
- use clean alignment for scanability

### 5) Schedule section
Add a schedule or plan panel showing upcoming workouts.

Suggested entries:
- Monday / HIIT / 7:00 AM
- Tuesday / Strength / 6:30 PM
- Wednesday / Recovery Yoga / 8:00 AM

Recommended presentation:
- vertically stacked schedule items
- each includes day/time, workout type, and optional duration/intensity chip
- maintain clear hierarchy so this reads like a real dashboard module

## Layout Strategy

### Desktop
Recommended arrangement:
- top overview hero spans full width
- below that, use a multi-column grid
- one column can hold progress + goals while another holds schedule, or use stacked sections with internal grids

Possible desktop flow:
1. hero overview
2. stats grid
3. two-column content area
   - left: progress cards + goals
   - right: schedule panel

### Tablet
- reduce grid columns
- maintain clear spacing between cards
- avoid overly narrow multi-card rows

### Mobile
- stack all sections vertically
- keep stats readable with 1–2 columns
- progress rows and schedule rows must remain easy to scan
- avoid cramped card content and tiny labels

## Visual Style Direction
Target a clean, high-energy fitness aesthetic.

Recommended design language:
- bright accent colors such as lime, teal, electric blue, coral, or vivid orange
- crisp, high-contrast typography
- layered cards with soft shadows
- rounded but disciplined card corners
- subtle gradients to create energy without clutter

Overall feel should be:
- active
- modern
- motivating
- dashboard-like rather than marketing-heavy

## Accessibility / Correctness Requirements
- use semantic headings for major dashboard sections
- ensure all links/buttons have visible `:focus-visible` states
- maintain sufficient contrast for stat values and progress indicators
- preserve logical reading order when cards collapse on mobile
- avoid relying on color alone to indicate goal completion; include numbers or labels

## Dark/Light Mode Strategy
Dashboard should support both modes if practical.

Recommended approach:
- define tokens in `:root`
- use a bright but controlled light theme by default
- provide a dark-mode override using `prefers-color-scheme: dark`
- ensure accent colors remain readable in both modes

## Suggested Content Plan

### Hero / overview
- title: weekly training summary
- supporting text about consistency or energy
- 2–3 compact chips or action-like pills

### Stats cards
- 18 workouts completed
- 8,420 calories burned
- 11h 40m active time
- 6-day streak

### Progress cards
- weekly movement progress
- strength target progress
- hydration progress

### Daily goals
- 10,000 steps
- 2.5L water
- 8h sleep
- protein target

### Schedule
- 3–5 upcoming workouts with day/time/type/duration

## Reliability / Regression Risks
Grunt should watch for:
- leftover restaurant-specific class names/styles leaking into the new dashboard
- progress bars looking inconsistent due to hardcoded widths without alignment rules
- stat cards becoming uneven if one label wraps more than others
- schedule rows becoming cramped on mobile widths
- accent colors losing contrast in dark mode
- decorative visuals stealing attention from primary data

## Suggested QA Checklist for Pedant
- verify the page clearly reads as a fitness app dashboard
- verify workout stats, progress cards, daily goals, and schedule sections are all present
- verify dashboard cards remain balanced across desktop, tablet, and mobile
- verify no horizontal overflow occurs
- verify focus states are visible on interactive elements
- verify progress visuals remain readable and not purely color-dependent
- verify the page feels energetic and clean rather than cluttered

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current page in `index.html` with a responsive fitness dashboard featuring an overview hero, workout stats, progress cards, daily goals, and a schedule section, all implemented with HTML and CSS only.
