# ARCHITECT PLAN — PAP-232

## Ticket
Create a modern calculator UI using HTML, CSS, and JavaScript.

## Role Scope
This is the **PLAN_DESIGN** phase only.

Allowed in this phase:
- inspect the repo and current implementation
- analyze requirements
- produce a concrete implementation plan for the next role
- leave handoff artifacts

Not allowed in this phase:
- implement UI or behavior changes
- modify calculator code in `index.html`
- create a PR
- push branches

## Repository / Stack Inspection
Observed files relevant to this ticket:
- `index.html`
- `README.md`
- prior handoff documents for earlier tickets

Current stack characteristics:
- single-page static app
- HTML, CSS, and JavaScript are all currently embedded in `index.html`
- no framework or build tooling is required for this ticket
- repo already appears optimized for a one-file deliverable

## Current State Assessment
The current `index.html` already contains a polished calculator implementation with:
- a responsive shell layout
- a styled display area
- digit and operator buttons
- JavaScript input/evaluation logic
- hover/focus interaction styling
- dark mode via `prefers-color-scheme`

Because the existing page is already in-domain for PAP-232, the safest implementation path is **refinement and verification rather than a full rebuild**.

## Scope Interpretation
PAP-232 requires a calculator that is:
- modern
- stylish
- responsive
- polished on desktop and mobile

Required functionality:
- addition
- subtraction
- multiplication
- division
- input handling
- clear/reset actions
- result output

Required design traits:
- well-designed display screen
- interactive buttons
- smooth hover effects
- clear visual hierarchy
- balanced spacing
- rounded buttons
- subtle shadows
- mobile-friendly layout
- optional dark mode styling

## Implementation Recommendation for Grunt
### Primary recommendation
Use the current `index.html` as the implementation base and do a targeted pass to:
1. verify the current UI against the exact ticket language
2. tighten any remaining UX/details gaps
3. keep the final solution self-contained in `index.html`

### Why this is the right path
- lowest-risk change surface
- aligns with existing project structure
- avoids unnecessary file churn
- likely meets the ticket faster with fewer regressions

## Concrete Build Plan

### 1) Preserve the one-file architecture
Keep HTML, CSS, and JavaScript in `index.html` unless there is a very strong reason to split files.

Expected result:
- simple delivery
- easy review
- no dependency/setup complexity

### 2) UI structure to preserve or refine
Recommended page structure:
- top-level centered calculator container
- compact app-like shell/card
- header block with title and supporting text
- display block with expression + result
- 4-column keypad grid
- optional small usage note for keyboard controls

Recommended element groups:
- page wrapper
- shell/card
- header
- display panel
- expression line
- result line
- keypad grid
- button variants for number / operator / utility / primary action

### 3) Visual design targets
The final UI should feel premium and contemporary.

Design direction:
- soft gradient or layered background
- elevated card surface
- rounded corners throughout
- subtle depth via shadows
- high-contrast result display
- differentiated operator and utility styling
- visually prominent equals action

Specific traits to confirm/refine:
- generous spacing between controls
- large readable display numerals
- button hover/press feedback
- consistent radii and shadow system
- balanced spacing at narrow widths

### 4) Functional behavior plan
JavaScript should support the following actions reliably:
- append digits
- append decimal point
- append operators
- delete last character
- clear all
- evaluate expression
- show result output

### 5) State management plan
Recommended state to track:
- `expression`
- `justEvaluated`
- `errorState`

Behavior expectations:
- entering a number after evaluation starts a fresh expression
- entering an operator after evaluation continues from the result
- clear always resets both state and display
- delete behaves safely when expression is empty or after errors

### 6) Input validation rules
Grunt should explicitly verify or refine the following:
- only calculator-safe characters are accepted
- one decimal per operand
- malformed trailing operators are not evaluated
- divide-by-zero shows a user-friendly error
- invalid expressions do not crash the page
- expression formatting is readable in the display

### 7) Responsive plan
#### Mobile
- calculator width should fit comfortably inside viewport
- buttons should remain easy to tap
- spacing should tighten slightly without feeling cramped
- result text should scale without overflow

#### Desktop/tablet
- shell remains centered and compact
- display retains emphasis
- buttons feel evenly sized and balanced

### 8) Dark mode plan
Dark mode is optional per ticket but desirable.

Recommendation:
- keep `prefers-color-scheme: dark` support
- verify readable contrast for:
  - labels
  - result text
  - utility buttons
  - operator buttons
  - primary equals button

### 9) Accessibility plan
Implementation should preserve or add:
- semantic `<button>` elements
- visible keyboard focus states
- `aria-live` on the display region if already present
- sufficient color contrast
- no information conveyed by color alone

### 10) Keyboard support plan
Not strictly required, but worth preserving if already implemented.

Recommended supported keys:
- `0-9`
- `+ - * /`
- `.`
- `Enter`
- `=`
- `Backspace`
- `Escape`

## Risks / Review Hotspots
Grunt and Pedant should pay special attention to:
- long expressions overflowing the display
- repeated decimal handling
- negative number input edge cases
- operator replacement/chaining behavior
- divide-by-zero handling
- inconsistent button sizing at mobile widths
- dark mode contrast regressions
- hover states feeling too aggressive on touch layouts

## Suggested Acceptance Checklist
- calculator performs `+`, `-`, `*`, `/` correctly
- `AC` resets everything cleanly
- `DEL` removes the last entry predictably
- display clearly distinguishes expression vs result
- hover/focus states are visible and polished
- UI looks modern on desktop and mobile
- dark mode remains legible and intentional
- page stays self-contained with no external dependencies

## Files for Next Role
Expected implementation file:
- `index.html`

Expected non-code artifact from this phase:
- `ARCHITECT_PLAN_PAP-232.md`

## Handoff to Grunt
Use the existing calculator in `index.html` as the baseline. Do not rebuild from scratch unless inspection during implementation shows a clear structural problem. Focus on validating against PAP-232 requirements, refining visual polish where needed, and preserving reliable input/evaluation behavior in a single-file solution.

## Handoff to Pedant
Test both functionality and finish quality. This ticket is not just about math correctness; it also requires modern presentation, responsive behavior, hover/focus feedback, and polished light/dark visual hierarchy.
