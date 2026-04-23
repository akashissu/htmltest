# ARCHITECT PLAN — PAP-230

## Ticket
Create a modern calculator UI using HTML, CSS, and JavaScript.

## Scope Summary
Build a clean, stylish, and responsive calculator that includes:
- a polished display screen
- interactive number and operator buttons
- support for addition, subtraction, multiplication, and division
- clear/reset behavior
- result output via JavaScript
- smooth hover/focus interactions
- mobile-friendly layout
- optional dark mode styling

Constraints:
- HTML, CSS, and JavaScript only
- no external libraries required
- this phase is planning only; no calculator implementation in this phase

## Current Stack / Structure Observations
Repository snapshot:
- Main frontend entrypoint is `index.html`
- The current page is a pet adoption landing section from PAP-229
- Styling is embedded directly in a `<style>` block inside `index.html`
- Existing repo patterns favor:
  - single-file implementations
  - CSS custom properties in `:root`
  - visually polished card-like layouts
  - responsive grids/flex layouts
  - optional dark-mode-aware styling

## High-Level Recommendation
Implement this ticket as a **full replacement of the current page in `index.html`** using a single self-contained HTML document with embedded CSS and JavaScript.

Why:
- the current page content is unrelated to calculator functionality
- the requested UI is a focused, app-like experience rather than a multi-section landing page
- a one-file implementation will match the existing repo style and keep the handoff simple for Grunt and Pedant

## Recommended App Structure
Build the calculator as a centered app shell with a compact, premium-feeling interface.

Suggested structure:
- `<main class="calculator-page">`
- `<section class="calculator-shell" aria-labelledby="calculator-title">`
- header / intro area
- calculator display area
- calculator keypad grid

Suggested class blocks:
- `.calculator-page`
- `.calculator-shell`
- `.calculator-header`
- `.calculator-display`
- `.display-expression`
- `.display-result`
- `.calculator-keypad`
- `.calc-button`
- `.calc-button--operator`
- `.calc-button--accent`
- `.calc-button--utility`
- `.calc-button--wide`

## Functional Requirements Plan
JavaScript should support a straightforward four-operation calculator flow.

### Core interactions
Support:
- number input (`0-9`)
- decimal input (`.`)
- operators (`+`, `-`, `×`, `÷` or internal `*`, `/`)
- equals action (`=`)
- clear all (`AC` or `C`)
- delete/backspace (`DEL`) if included

### Recommended interaction model
Use a simple expression-building model with guarded evaluation.

Recommended state tracking:
- current expression string
- current displayed result/value
- flag for whether the last action was evaluation
- optional error state

### Evaluation behavior
Use JavaScript to:
- append numbers/operators to the expression safely
- prevent invalid repeated operators where practical
- handle decimal input without duplicating decimals in the current operand
- evaluate on equals
- display a friendly error state for invalid or unsafe expressions
- reset cleanly after clear

### Reliability guidance
Grunt should avoid overengineering. For this ticket, a guarded `Function(...)` or similar expression evaluation approach can work if inputs are fully limited to calculator buttons and sanitized first. If using this approach, sanitize operator symbols and disallow arbitrary characters before evaluation.

## Information Architecture Plan

### 1) App header
Recommended contents:
- title such as “Modern Calculator” or “Quick Math, Beautifully Done”
- short supporting line about fast everyday calculations

This should set the tone without taking too much vertical space.

### 2) Display block
The display is the most important visual element.

Recommended sub-elements:
- smaller line for the current expression / previous entry
- larger line for the active result/value

Display requirements:
- right-aligned text
- strong visual separation from keypad
- enough height for large, readable numbers
- overflow handling for long expressions

### 3) Keypad grid
Recommended keypad contents:
- top row: `AC`, `DEL`, `%` optional, `÷`
- middle rows: digits and arithmetic operators
- bottom row: `0`, `.`, `=` and remaining operator layout as needed

If `%` is not implemented, omit it rather than faking incomplete functionality.

Recommended baseline set:
- `AC`
- `DEL`
- `÷`
- `7 8 9 ×`
- `4 5 6 -`
- `1 2 3 +`
- `0 . =`

Use a balanced grid, likely 4 columns.

## Layout Strategy

### Desktop
- center the calculator on the page
- use a card/surface container with generous padding
- keep width compact enough to feel like a real calculator app

### Tablet
- preserve the centered composition
- slightly reduce padding and gap sizes if needed

### Mobile
- calculator should fit comfortably within the viewport width
- buttons should remain easy to tap
- maintain generous touch targets and avoid cramped spacing

## Visual Style Direction
Target a premium modern utility aesthetic.

Recommended design language:
- layered glass or soft card surface
- subtle gradients in the page background
- rounded display and button shapes
- gentle shadows for depth
- strong visual hierarchy between utility, number, and operator buttons

Recommended button styling split:
- number buttons: neutral elevated surface
- operator buttons: distinct accent color or tinted surface
- primary action (`=`): strongest accent emphasis
- utility buttons (`AC`, `DEL`): lower-emphasis but still clearly interactive

Overall feel should be:
- modern
- polished
- clear
- tactile

## Accessibility / Correctness Requirements
- use semantic button elements for all keypad controls
- ensure visible `:focus-visible` states for keyboard users
- maintain sufficient contrast for display text and buttons
- keep button labels clear and legible
- ensure layout does not overflow on small screens
- do not rely on color alone to distinguish button meaning; use position and labels too

## JavaScript Behavior Checklist
Grunt should implement and verify:
- clicking buttons updates the display correctly
- clear resets both expression and result state
- delete removes the last valid input
- equals computes correct results for supported arithmetic
- division by zero is handled gracefully
- invalid expressions do not crash the UI
- calculator recovers properly after an error

## Dark/Light Mode Strategy
Recommended approach:
- define color tokens in `:root`
- use a bright, clean default theme
- add a `prefers-color-scheme: dark` override for a darker modern variant
- keep accent colors readable in both modes

## Reliability / Regression Risks
Grunt should watch for:
- long expressions overflowing or clipping badly in the display
- duplicated decimal points in the same operand
- multiple operators entered back-to-back causing invalid evaluation
- equals behavior becoming inconsistent after a prior result
- division by zero showing raw JavaScript oddities instead of a clean error message
- button layout becoming uneven on narrow screens
- hover/focus states looking inconsistent between button types

## Suggested QA Checklist for Pedant
- verify calculator supports addition, subtraction, multiplication, and division
- verify clear/reset behavior works reliably
- verify result output updates correctly after sequential inputs
- verify the display remains readable on mobile and desktop
- verify the visual hierarchy between display, numbers, utilities, and operators is clear
- verify no horizontal overflow occurs
- verify dark mode remains legible if implemented
- verify invalid states are handled without breaking the interface

## Files Expected to Change in Grunt Phase
- `index.html`

## Artifact for Next Role
Grunt should replace the current pet adoption page in `index.html` with a responsive modern calculator interface built in HTML, CSS, and JavaScript. The implementation should include a polished display, a four-column keypad, support for `+`, `-`, `*`, and `/`, clear/reset behavior, result evaluation, visible interaction states, and resilient handling for common input edge cases.
