# ARCHITECT PLAN — PAP-231

## Ticket
Create a modern calculator UI using HTML, CSS, and JavaScript.

## Scope Summary
Build a calculator experience that is:
- clean
- stylish
- responsive
- modern-looking

Required functionality:
- addition
- subtraction
- multiplication
- division
- clear/reset handling
- result output with JavaScript

Required UI characteristics:
- polished display screen
- interactive buttons
- smooth hover effects
- clear visual hierarchy
- balanced spacing
- rounded buttons
- subtle shadows
- mobile-friendly layout
- optional dark mode styling

Constraints:
- HTML + CSS + JavaScript only
- no external dependencies needed
- this phase is planning only; do not implement code in this phase

## Current Stack / Structure Observations
Repository snapshot:
- Main entrypoint is `index.html`
- Styling and behavior currently live inline in the same file
- The current page already presents a calculator-style implementation from a prior ticket
- Existing repo conventions still favor:
  - one-file page delivery
  - design tokens in `:root`
  - embedded `<style>` and `<script>` blocks
  - responsive, polished UI work without frameworks

## High-Level Recommendation
Treat PAP-231 as a **calculator refinement/rebuild in `index.html`**, not an incremental tweak to unrelated content.

Why:
- the ticket is identical in shape to the current app domain, so work should stay focused in the same file
- a single-file implementation remains the simplest handoff path
- Grunt can either keep and improve the existing calculator if it already satisfies most requirements, or replace it if that is cleaner and safer

## Recommended Product Shape
The end result should feel like a compact calculator app rather than a generic demo.

Suggested page structure:
- `<main class="calculator-page">`
- `<section class="calculator-shell" aria-labelledby="calculator-title">`
- `<header class="calculator-header">`
- calculator display module
- keypad grid
- optional helper note for keyboard usage

Suggested class blocks:
- `.calculator-page`
- `.calculator-shell`
- `.calculator-header`
- `.calculator-display`
- `.display-label`
- `.display-expression`
- `.display-result`
- `.calculator-keypad`
- `.calc-button`
- `.calc-button--utility`
- `.calc-button--operator`
- `.calc-button--accent`
- `.calc-button--danger`
- `.calc-button--wide`

## Functional Plan
JavaScript should manage the calculator state cleanly and predictably.

### Minimum supported actions
- input digits `0–9`
- input decimal point
- input operators `+`, `-`, `*`, `/`
- evaluate expression with `=`
- clear everything with `AC`
- remove the last entry with `DEL`

### Recommended state model
Track:
- current expression string
- whether the previous action was evaluation
- whether the UI is currently showing an error state
- current result/output string

### Input rules
Grunt should make input handling resilient by:
- preventing repeated decimals within one operand
- preventing malformed operator sequences where practical
- allowing a leading minus for negative values if supported cleanly
- resetting correctly after clear and after an error
- allowing continued calculation from the most recent result after evaluation

### Evaluation plan
Recommended approach:
- limit all input to calculator-safe characters only
- sanitize before evaluation
- convert displayed operators to JavaScript-safe operators if needed
- reject obviously malformed expressions before evaluation
- show a friendly error for invalid math or divide-by-zero cases

## Information Architecture Plan

### 1) Header area
Recommended contents:
- short eyebrow or label identifying the calculator
- strong headline such as “Quick math, beautifully done”
- brief supporting copy

This should establish tone without crowding the calculator itself.

### 2) Display module
This is the most important visual block.

Recommended contents:
- small label and line for expression history/current expression
- large result line for the active output

Display requirements:
- right-aligned text
- distinct contrast from keypad area
- enough height for large numerals
- wrapping/overflow handling for long expressions
- visible error styling when needed

### 3) Keypad grid
Recommended arrangement: 4-column grid.

Suggested baseline rows:
- `AC`, `DEL`, `÷`, `×`
- `7`, `8`, `9`, `−`
- `4`, `5`, `6`, `+`
- `1`, `2`, `3`, `=`
- `0` (wide), `.`

Notes:
- avoid duplicate operator buttons unless there is a clear reason
- use semantic `<button>` elements only
- make the `=` button visually primary

## Layout Strategy

### Desktop
- center the calculator within the viewport
- keep width compact and app-like
- maintain generous padding around the shell and display

### Tablet
- preserve centered alignment
- reduce button and shell spacing slightly if needed

### Mobile
- keep the calculator fully within viewport width
- preserve comfortable tap targets
- ensure the button grid remains balanced and uncluttered

## Visual Style Direction
Aim for a premium utility aesthetic.

Recommended design language:
- soft glassmorphism or elevated card surface
- layered gradients in page background
- rounded buttons and display edges
- subtle but noticeable shadows
- crisp contrast between background, shell, display, and button groups

Suggested visual hierarchy:
- result display = strongest emphasis
- operators = clearly differentiated accent treatment
- utility actions = toned but noticeable
- equals button = highest action emphasis

Overall feel should be:
- modern
- tactile
- elegant
- easy to scan

## Accessibility / Correctness Requirements
- use semantic buttons for all calculator controls
- preserve visible `:focus-visible` states
- ensure contrast is sufficient in both light and dark themes
- do not rely only on color to separate utilities/operators/numbers
- ensure no horizontal overflow on small screens
- keep text readable at all supported sizes

## Keyboard Support Recommendation
Keyboard support is not explicitly required by the ticket, but if already present or easy to preserve, it should be retained.

Recommended supported keys:
- digits
- `+`, `-`, `*`, `/`
- `.`
- `Enter` or `=`
- `Backspace`
- `Escape`

## Reliability / Regression Risks
Pedant should pay special attention to:
- duplicated decimal points slipping through
- malformed operator chains causing broken evaluation
- divide-by-zero showing `Infinity` instead of a clean error
- result state not resetting correctly after an error
- expression/result text becoming unreadable with long inputs
- uneven grid alignment on narrow screens
- dark mode reducing contrast too much for labels or utility buttons

## Suggested QA Checklist for Pedant
- verify all four arithmetic operations work correctly
- verify `AC` fully resets state and display
- verify `DEL` removes the last character appropriately
- verify `=` evaluates valid expressions and handles invalid ones safely
- verify divide-by-zero yields a friendly error state
- verify buttons have hover and focus-visible states
- verify no horizontal overflow occurs on mobile widths
- verify the calculator remains visually polished in both light and dark mode if dark mode is included

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should deliver a polished calculator in `index.html`, either by refining the existing implementation or replacing it cleanly. The final UI should include a prominent display, responsive 4-column keypad, differentiated operator/utility/action buttons, working JavaScript arithmetic, reliable clear/delete/error handling, and a mobile-friendly modern visual treatment.
