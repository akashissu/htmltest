# ARCHITECT PLAN — PAP-238

## Ticket
Create a modern Tic Tac Toe game using HTML, CSS, and JavaScript.

## Phase Scope
This phase is planning only.

Allowed in this phase:
- inspect the current repository and implementation shape
- assess scope, risks, and likely refinement targets
- produce a concrete implementation plan for Grunt
- identify review targets for Pedant

Not allowed in this phase:
- edit `index.html`
- implement UI, CSS, or JavaScript changes
- create a PR
- push branches

## Current Stack Assessment
Observed repository shape:
- single static page app
- HTML, CSS, and JavaScript embedded in `index.html`
- no build tooling or dependencies required

Current file state:
- `index.html` already contains a polished Tic Tac Toe implementation
- the app includes a 3x3 board, status panel, restart controls, theme toggle, and responsive styling

## Scope Interpretation
PAP-238 should be treated as a refinement and verification pass, not a full rebuild.

Requested end result:
- modern Tic Tac Toe experience
- 3x3 interactive grid
- turn-based X/O play
- invalid move prevention
- win and draw detection
- reset/restart control
- polished responsive UI
- clear game status/result messaging
- optional dark mode styling

## Recommended Delivery Strategy
### Primary recommendation
Use the existing `index.html` as the only implementation target and refine only where correctness, UX, or reliability improvements are still needed.

### Why
- current implementation already matches most of the ticket
- lowest-risk path is targeted refinement
- keeps the repository aligned with its one-file structure

## Current Implementation Strengths
The current page already provides:
- centered modern game shell
- responsive 3x3 button-based board
- turn switching for X and O
- win detection and winning-cell highlighting
- draw detection
- restart / clear-board controls
- keyboard shortcuts and focusable cells
- explicit dark mode toggle with persistence
- polished hover/focus/press interactions

## Likely Refinement Opportunities for Grunt
### 1) Clarify reset semantics
There are currently two controls:
- `Restart game`
- `Clear board`

Grunt should confirm and, if needed, tighten behavior so labels and actions are fully intuitive.

Recommended semantics:
- `Restart game` → always resets to an empty board with X starting
- secondary action should either:
  - clearly start the next round with alternating starter, or
  - be simplified/renamed if the current behavior feels ambiguous

### 2) Verify game-state messaging consistency
Ensure the status panel always reflects the true state:
- X turn
- O turn
- X win
- O win
- draw

Potential improvement:
- status badge text could distinguish `Turn`, `Winner`, and `Draw` more explicitly if helpful

### 3) Check board lock behavior after game over
Current implementation disables all cells after game over.
Grunt should verify this remains visually clear and accessible.

Potential refinement:
- preserve winner highlight while dimming non-winning cells in a controlled way
- ensure disabled cells do not feel broken or inaccessible

### 4) Validate keyboard behavior
Current implementation supports:
- native button activation for cells
- `T` theme toggle
- `R` restart

Grunt should verify no conflicts or accidental triggers exist.

### 5) Preserve responsiveness and visual polish
Focus on maintaining:
- square cells on small screens
- no overflow
- balanced spacing across header, status, board, controls
- strong contrast in dark mode

## Concrete Plan for Grunt

### 1) Keep the single-file structure
Implementation target:
- `index.html`

Do not split CSS or JavaScript into separate assets.

### 2) Perform a refinement pass, not a rewrite
Keep the existing game structure and improve only where needed:
- header
- status panel
- board
- controls
- theme behavior
- game state transitions

### 3) Audit control semantics
Review whether the two control buttons are both necessary and clearly named.
If the secondary control behavior is confusing, simplify it.

### 4) Verify core logic paths
JavaScript should reliably handle:
- valid move placement
- invalid move rejection
- turn alternation
- all 8 winning lines
- draw detection only when no winner exists
- full reset of board/state
- no moves after game over

### 5) Improve clarity where safe
Possible polish improvements:
- more explicit status copy
- clearer button labels
- slightly stronger winning-state emphasis
- accessibility wording improvements for cells/status

### 6) Preserve theme support
Keep system dark-mode compatibility and explicit theme toggle if retained.
If refined, ensure:
- persistent user selection remains intact
- button/icon labels stay accurate
- contrast remains strong in both themes

## Risks / Hotspots for Grunt
Most likely issues to inspect:
- ambiguous `Clear board` behavior
- incorrect starter selection after certain resets
- draw detection occurring after a winning move in edge ordering
- status text lagging behind actual state
- post-game interactions not fully locked or visually consistent

## Review Hotspots for Pedant
Pedant should verify:
- all 8 winning lines fire correctly
- draw only occurs when no winner exists
- reset behavior is intuitive and consistent
- no extra move is possible after game over
- status messaging matches actual state at all times
- mobile layout remains square and overflow-free
- dark mode contrast and theme persistence remain reliable

## Suggested Acceptance Checklist
- board renders as a 3x3 grid
- X and O alternate correctly
- filled cells cannot be overwritten
- all row/column/diagonal wins are detected
- draw is detected correctly
- reset/restart behavior is intuitive and correct
- UI is polished and responsive
- status text is always accurate
- dark mode styling is coherent if included

## Handoff to Grunt
Start from the existing `index.html`. Prefer a minimal refinement pass focused on correctness, state clarity, and control semantics rather than a redesign.

## Handoff to Pedant
Review win/draw logic exhaustively, verify reset semantics, confirm no post-game moves are possible, and check responsiveness and dark-mode readability.

## Phase Artifact
Produced in this phase:
- `ARCHITECT_PLAN_PAP-238.md`
