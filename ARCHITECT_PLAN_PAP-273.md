# Architect Plan — PAP-273

## Scope Summary
Build a **weather app UI** using **HTML and CSS only**. The interface should include:
- a search bar
- current temperature display
- condition icon / visual weather indicator
- forecast cards

The result should be simple, clear, readable, and polished.

## Current Stack Inspection
- Current sandbox is a **static single-page HTML file** with embedded CSS in `index.html`.
- No framework, asset pipeline, or reusable component library is active for this task.
- Safest implementation path: **replace the current unrelated page in `index.html` with a self-contained weather UI**.

## Product Goal
Create a lightweight dashboard-style weather interface that communicates the current conditions at a glance and shows a short forecast in an easy-to-scan layout.

## Layout Plan
### Main structure
1. **App shell / card container**
   - centered weather panel with soft background and rounded corners
2. **Top bar**
   - app title or location label
   - search bar for city lookup (UI only; no functionality required)
3. **Current weather section**
   - prominent temperature
   - condition label (e.g. Sunny / Cloudy / Rainy)
   - large icon or CSS weather symbol
   - optional high/low summary
4. **Forecast section**
   - 4–5 compact forecast cards
   - each card includes day, icon, temperature range, short condition

## Visual Direction
### Tone
- Calm, airy, modern
- Emphasis on readability over decoration
- Use a soft sky-inspired palette

### Palette suggestion
- pale sky / blue gradient background
- white glassy panel or bright card surface
- deep navy or slate text
- accent colors:
  - sunny: warm yellow
  - cloudy: muted gray-blue
  - rainy: cool blue

### Design details
- soft shadows
- rounded cards
- generous whitespace
- large temperature typography
- compact, consistent forecast cards

## Suggested Content
### Current weather example
- Location: San Francisco, CA
- Temperature: 24°C
- Condition: Sunny with light breeze
- High/Low: H: 26°C · L: 18°C

### Forecast example
- Mon — 25° / 18° — Sunny
- Tue — 23° / 17° — Cloudy
- Wed — 21° / 16° — Rainy
- Thu — 24° / 18° — Partly cloudy
- Fri — 26° / 19° — Sunny

## Accessibility Requirements
- Use semantic structure (`main`, `section`, `header`, `form`, `article`)
- Ensure search input has a visible label or accessible label
- Maintain strong text contrast
- Keep icon treatment decorative unless it conveys unique meaning; if using text symbols, ensure adjacent text already conveys condition
- Provide visible focus styles for the search input and button

## Responsive Plan
### Desktop
- current conditions and forecast can sit in stacked sections inside a centered panel
- forecast cards in a horizontal or multi-column grid

### Tablet
- maintain centered layout
- forecast cards wrap cleanly to multiple rows if needed

### Mobile
- single-column stack
- search field full width
- current weather remains the visual priority
- forecast cards remain easy to scan without horizontal scrolling

## CSS Implementation Plan
### Core tokens
Define CSS custom properties for:
- background gradient
- surface/card color
- text primary / secondary
- accent colors
- border radius
- shadow

### Styling areas
1. **Page background**
   - light sky gradient
2. **App shell**
   - centered panel with rounded corners and shadow
3. **Search area**
   - compact search input with optional button
4. **Current weather block**
   - oversized temperature
   - condition row
   - simple icon built with emoji or CSS shape styling
5. **Forecast cards**
   - uniform small cards with day, icon, temps, condition

## Minimal Safe Implementation Strategy
1. Replace current unrelated content in `index.html`
2. Keep the UI fully self-contained in HTML/CSS
3. Do not add JavaScript since the ticket only requests UI
4. Use emoji or CSS-based icons to avoid external assets

## Edge Cases / Review Targets for Pedant
- Verify forecast cards wrap cleanly at narrow widths
- Confirm temperature text does not overflow on mobile
- Check search bar alignment and focus visibility
- Ensure icons don’t reduce readability or spacing consistency

## Grunt Handoff Checklist
- [ ] Replace current page with weather app UI
- [ ] Add search bar
- [ ] Add current temperature + condition icon area
- [ ] Add 4–5 forecast cards
- [ ] Keep it simple and easy to read
- [ ] Leave Pedant handoff notes and terminal log

## Suggested Deliverables
- Updated `/tmp/zero-human-sandbox/index.html`
- `/tmp/zero-human-sandbox/PEDANT_HANDOFF_PAP-273.md`
- `/tmp/zero-human-sandbox/TERMINAL_LOGS_PAP-273_GRUNT.txt`
