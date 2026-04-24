# ARCHITECT PLAN — PAP-234

## Ticket
Create a modern calculator UI using HTML, CSS, and JavaScript.

## Role Scope
This phase is planning only.

Allowed:
- inspect the current repository and existing implementation
- analyze requirement coverage and risk areas
- produce a concrete implementation plan for the next role
- leave a handoff artifact

Not allowed:
- modify `index.html` feature code in this phase
- implement UI or JavaScript changes
- create a PR
- push branches

## Current Repository Assessment
Relevant files observed:
- `index.html`
- prior handoff notes for similar calculator tickets
- `README.md`

Current stack:
- static single-page app
- inline HTML, CSS, and JavaScript in `index.html`
- no framework, package manager, or build step needed
- suitable for a self-contained calculator deliverable

## Current Implementation Assessment
The current `index.html` already contains a calculator experience with:
- centered card-style layout
- polished display area
- calculator keypad
- JavaScript arithmetic logic
- hover/focus states
- responsive sizing
- dark mode via system preference

This means PAP-234 should be approached as a **targeted refinement and verification task**, not a blank-slate build.

## Scope Interpretation
Required outcomes:
- clean, stylish, modern calculator
- responsive layout
- basic arithmetic: addition, subtraction, multiplication, division
- display screen for expression/result
- interactive buttons with smooth hover states
- balanced spacing and rounded controls
- subtle shadows and clear hierarchy
- JavaScript-driven input, clear/reset, calculations, and result output
- optional dark mode styling

## Recommended Delivery Strategy
### Primary recommendation
Use the existing `index.html` as the base and refine only where needed.

### Why
- lowest-risk path
- aligns with repository structure
- easiest to validate and hand off
- likely requires only polish and edge-case tightening rather than rebuild work

## Concrete Plan for Grunt

### 1) Keep the one-file implementation
Primary target:
- `index.html`

Avoid splitting files unless an unexpected issue makes it necessary.

### 2) Preserve and refine page structure
Recommended structure to keep or improve:
- page wrapper
- calculator shell/card
- header block
- display module with expression and result
- 4-column keypad grid
- optional compact usage note

### 3) Visual design goals
Target feel:
- premium utility app
- soft gradient or layered backdrop
- elevated shell/card
- large clear result display
- rounded corners and balanced spacing
- distinct button styles for numbers, utilities, operators, and equals
- subtle but noticeable hover/press states

### 4) Functional behavior goals
JavaScript should reliably support:
- digit entry `0–9`
- decimal entry
- operators `+`, `-`, `*`, `/`
- equals evaluation
- all-clear reset
- delete/backspace

### 5) State handling goals
Expected state model:
- `expression`
- `justEvaluated`
- `errorState`

Expected behaviors:
- entering a number after evaluation starts fresh
- entering an operator after evaluation continues from the result
- errors are recoverable via clear or next valid action
- invalid input sequences do not break the interface

### 6) Input validation goals
Grunt should confirm or refine:
- one decimal per operand
- malformed trailing operators are not evaluated
- negative numbers are handled sensibly
- divide-by-zero produces a friendly error
- display formatting remains readable for long expressions

### 7) Responsive behavior goals
#### Mobile
- no horizontal overflow
- comfortable tap targets
- layout stays centered and uncluttered
- text remains legible

#### Desktop / tablet
- compact, centered shell
- strong hierarchy in the display area
- evenly balanced keypad grid

### 8) Dark mode goals
Dark mode is optional but recommended.

Recommendation:
- preserve system dark mode support
- optional explicit theme toggle is acceptable if it is implemented cleanly
- verify contrast for labels, result text, and button variants

### 9) Accessibility goals
Implementation should preserve or add:
- semantic buttons
- visible focus states
- adequate contrast
- `aria-live` for display updates if already present
- no reliance on color alone for critical meaning

## Review Hotspots for Pedant
Pedant should inspect:
- operator chaining edge cases
- repeated decimals
- negative operand sequences
- divide-by-zero handling
- behavior after errors/evaluation
- long expression wrapping
- mobile spacing and overflow
- dark mode readability

## Suggested Acceptance Checklist
- all four arithmetic operations work correctly
- `AC` resets fully
- `DEL` removes the last entry correctly
- invalid expressions do not crash the app
- divide-by-zero shows a human-friendly message
- buttons have polished hover/focus/active feedback
- layout looks balanced on desktop and mobile
- dark mode is readable and intentional if present

## Files Expected Next Phase
Primary implementation target:
- `index.html`

Artifact produced in this phase:
- `ARCHITECT_PLAN_PAP-234.md`

## Handoff to Grunt
Use the current `index.html` as the starting point. Avoid a rebuild unless a structural issue appears during implementation. Focus on small, safe refinements that improve ticket coverage and polish.

## Handoff to Pedant
Review both correctness and presentation quality. This ticket requires reliable arithmetic behavior plus a convincingly modern, responsive, polished UI.
