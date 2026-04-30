# Architect Plan — PAP-271

## Scope Summary
Create a **recipe cards section** using **HTML and CSS only**. The design should be colorful, appetizing, and easy to scan, with each card including:
- food image area
- recipe title
- cooking time
- short description

## Current Stack Inspection
- Current sandbox uses a **single `index.html` file** with embedded `<style>`.
- No active framework, component library, or asset pipeline is present for this task.
- Safest implementation path: **replace the current unrelated page content with a self-contained recipe cards layout in `index.html`**.

## Product Goal
Build a visually appealing recipe discovery section that feels bright and fresh, like a modern food blog or meal app landing section.

## Design Direction
### Visual tone
- Warm, colorful, inviting
- Fresh palette inspired by food:
  - tomato / coral accent
  - leafy green accent
  - cream or pale peach background
  - deep charcoal for text
- Soft shadows and rounded cards
- Playful but clean typography hierarchy

### Layout direction
Use a simple content structure:
1. **Section intro / heading area**
   - eyebrow or small label
   - main heading
   - short supporting text
2. **Responsive recipe card grid**
   - 3 cards on desktop if space allows
   - 2 cards on tablet
   - 1 card on mobile

## Card Structure
Each recipe card should contain:
- decorative food image block (CSS gradient/mock image area if no real assets)
- recipe title
- cooking time row with icon/text treatment
- short description (1–2 lines)
- optional secondary metadata like difficulty or cuisine only if it doesn’t clutter

## Suggested Example Recipes
- Spicy Tomato Pasta — 25 min
- Citrus Salmon Bowl — 30 min
- Garden Veggie Tacos — 20 min
- Honey Berry Toast — 10 min

## Accessibility Requirements
- Use semantic structure: `main`, `section`, `article`, heading hierarchy
- Ensure strong contrast for text on colorful backgrounds
- Avoid putting critical text inside decorative image areas
- Add visible focus states if cards or buttons are interactive
- If image areas are decorative only, no alt text is needed; if actual `img` tags are used, provide descriptive alt text

## Responsive Plan
### Desktop
- Wide centered section
- 3-column grid with even card heights
- Spacious padding and larger heading

### Tablet
- 2-column card layout
- Slightly reduced spacing

### Mobile
- Single-column stack
- Maintain image aspect ratio
- Keep cooking time and description readable without crowding

## CSS Implementation Plan
### Core tokens
Define CSS custom properties for:
- page background
- card background
- text primary / muted
- accent warm / accent fresh
- border radius
- shadow
- spacing

### Styling areas
1. **Page background**
   - soft food-inspired gradient or solid warm neutral
2. **Intro block**
   - bold headline + muted description
3. **Recipe cards**
   - rounded container
   - decorative image area with bright gradient overlays
   - title/time/description rhythm
4. **Metadata styling**
   - cooking time chip or compact inline badge
5. **Hover polish**
   - subtle lift on card hover
   - preserve reduced-motion behavior where possible

## Minimal Safe Implementation Strategy
Because the repo is a static single-file page:
1. Replace unrelated existing content in `index.html`
2. Keep HTML and CSS self-contained
3. Do not introduce JavaScript
4. Use CSS-only placeholder image blocks to avoid external dependencies and broken assets

## Edge Cases / Review Targets for Pedant
- Confirm cards do not overflow on narrow screens
- Check heading wrap behavior at mobile widths
- Verify text remains readable on colorful image placeholders
- Ensure spacing is balanced if descriptions vary in length
- Review focus styles if cards or CTAs are made interactive

## Grunt Handoff Checklist
- [ ] Replace current unrelated page with recipe cards section
- [ ] Add section intro with colorful visual identity
- [ ] Add 3–4 recipe cards with image area, title, cooking time, description
- [ ] Add responsive CSS for desktop/tablet/mobile
- [ ] Keep implementation HTML/CSS only
- [ ] Leave Pedant handoff notes and terminal log artifact

## Suggested Deliverables
- Updated `/tmp/zero-human-sandbox/index.html`
- `/tmp/zero-human-sandbox/PEDANT_HANDOFF_PAP-271.md`
- `/tmp/zero-human-sandbox/TERMINAL_LOGS_PAP-271_GRUNT.txt`
