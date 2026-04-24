# ARCHITECT PLAN — PAP-237

## Ticket
Create a modern Tic Tac Toe game using HTML, CSS, and JavaScript.

## Phase Scope
This phase is planning only.

Allowed in this phase:
- inspect the current repository and implementation shape
- assess scope, constraints, and likely risks
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
- `index.html` currently contains a calculator implementation, not Tic Tac Toe

## Scope Interpretation
PAP-237 is not a refinement of the current calculator. It is effectively a **single-page replacement** task inside the existing one-file structure.

Required end result:
- a modern Tic Tac Toe game
- 3x3 interactive board
- turn-based X/O gameplay
- prevention of invalid moves
- win detection
- draw detection
- reset/restart control
- polished responsive UI
- clear game status/result messaging
- optional dark mode styling

## Recommended Delivery Strategy
### Primary recommendation
Replace the current calculator experience in `index.html` with a self-contained Tic Tac Toe experience while preserving the single-file architecture.

### Why
- current app content does not match the new ticket domain
- simplest path is a direct one-file rewrite rather than partial adaptation
- keeps implementation aligned with repository expectations

## Concrete Plan for Grunt

### 1) Keep the one-file structure
Implementation target:
- `index.html`

Do not split CSS/JS into separate assets unless absolutely necessary.

### 2) Replace calculator-specific UI with a game layout
Recommended page structure:
- page wrapper / centered shell
- compact game header
- title + short helper copy
- optional theme toggle if added safely
- status panel showing current turn / outcome
- 3x3 board grid
- restart/reset control row
- optional lightweight footer note for controls or turn guidance

### 3) Visual design goals
Aim for:
- modern soft-card or glassy shell styling
- balanced spacing and strong visual hierarchy
- large readable X/O marks
- rounded board cells with subtle shadows
- smooth hover/focus/press states
- distinct visual treatment for active game state, winning state, and disabled/finished state
- mobile-friendly tap targets

### 4) Game state model
Recommended JavaScript state:
- `board`: array of 9 entries
- `currentPlayer`: `'X'` or `'O'`
- `winner`: `null | 'X' | 'O'`
- `isDraw`: boolean
- `isGameOver`: boolean

Optional state if a theme toggle is added:
- persisted theme preference in localStorage

### 5) Core interaction behavior
JavaScript should handle:
- clicking empty cells to place the current player mark
- ignoring clicks on filled cells
- ignoring clicks after game over
- toggling turns after valid moves only
- detecting a winner after each move
- detecting a draw when all cells are filled without a winner
- resetting the board and state when restart is pressed

### 6) Win detection approach
Recommended method:
- define the 8 winning line combinations
- after each valid move, test whether the current player controls any complete line
- if yes, mark game as over and display winner
- if no winner and board full, mark draw

Suggested winning lines:
- rows: `[0,1,2]`, `[3,4,5]`, `[6,7,8]`
- columns: `[0,3,6]`, `[1,4,7]`, `[2,5,8]`
- diagonals: `[0,4,8]`, `[2,4,6]`

### 7) Status and feedback guidance
Display area should clearly communicate:
- whose turn it is during play
- when X wins
- when O wins
- when the game ends in a draw

Recommended optional enhancements:
- highlight the winning cells
- subtly dim inactive board state after game end
- keep messaging concise and visible above the board

### 8) Accessibility expectations
Implementation should include:
- semantic button elements for cells and restart control
- visible keyboard focus states
- clear status text outside color alone
- enough contrast in both light and dark modes
- optional `aria-live="polite"` for status updates
- board usable on keyboard if practical via button cells

### 9) Responsive behavior goals
Mobile:
- square board remains centered and fully visible
- cells stay large enough for touch input
- no horizontal overflow
- status and restart controls remain readable

Desktop/tablet:
- board stays compact and visually balanced
- card layout remains centered and polished
- supporting text does not overpower the board

### 10) Optional theme control
Dark mode is optional but recommended.
Possible safe approaches:
- support `prefers-color-scheme`
- optionally add a small theme toggle with persistence

If added, ensure:
- high contrast for X and O marks
- board borders and buttons remain clear
- hover/focus states are still legible

## Risks / Hotspots for Grunt
Most likely implementation pitfalls:
- allowing moves after game over
- failing to block already-filled cells
- off-by-one issues in win detection
- status text not syncing with state
- reset not fully clearing board/result state
- board cells losing square proportions on small screens

## Review Hotspots for Pedant
Pedant should verify:
- every winning line is detected correctly
- draw detection only happens when no winner exists
- invalid move prevention is reliable
- reset fully restores initial state
- no extra move is possible after win/draw
- winning highlight, if added, matches the actual line
- keyboard focus states are visible
- mobile layout has no overflow
- dark mode remains readable if present

## Suggested Acceptance Checklist
- board renders as a 3x3 grid
- players alternate X and O correctly
- filled cells cannot be overwritten
- winner is detected for rows, columns, and diagonals
- draw is detected correctly
- restart button resets the game fully
- UI is polished, responsive, and mobile-friendly
- buttons/cells have hover/focus/active feedback
- status text is always accurate
- dark mode styling is coherent if included

## Handoff to Grunt
Replace the current calculator UI in `index.html` with a polished single-file Tic Tac Toe implementation. Prioritize correct game logic first, then polish, responsiveness, and optional theme support.

## Handoff to Pedant
Review win/draw logic exhaustively, invalid move prevention, post-game lockout, reset behavior, responsiveness, and dark-mode readability if implemented.

## Phase Artifact
Produced in this phase:
- `ARCHITECT_PLAN_PAP-237.md`
