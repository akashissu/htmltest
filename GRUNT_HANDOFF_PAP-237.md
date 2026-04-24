# GRUNT HANDOFF — PAP-237

## What I changed
Replaced the calculator in `index.html` with a single-file Tic Tac Toe game that matches the ticket scope.

### UI / UX updates
- replaced the calculator shell with a polished Tic Tac Toe layout
- added a responsive 3x3 game board built from semantic button cells
- added a live status panel for in-play / winner / draw states
- added restart and clear-board controls
- added an explicit light/dark theme toggle with persistence
- preserved a modern glass-card visual style with rounded elements, shadows, and hover/focus feedback

### Behavior / reliability updates
- implemented turn-based gameplay for X and O
- blocked invalid moves on filled cells
- blocked further moves after win or draw
- added row / column / diagonal win detection
- added draw detection when the board fills without a winner
- added winning-cell highlight state
- made restart fully reset board and game state
- kept keyboard accessibility via button cells and added theme/restart shortcuts (`T`, `R`)

## Files changed
- `index.html`

## Files added
- `GRUNT_HANDOFF_PAP-237.md`

## Validation performed
- JavaScript syntax check passed
- local HTTP smoke test passed
- confirmed expected Tic Tac Toe markers are present in served HTML (`status-message`, final board cell, theme storage key)

## Notes for Pedant
Please verify:
- X and O alternate correctly after each valid move
- filled cells cannot be played again
- no moves are accepted after win or draw
- all 8 winning lines are detected correctly
- draw detection occurs only when appropriate
- winning highlight matches the actual winning line
- `Restart game` fully resets to an empty board with X starting
- `Clear board` behavior is acceptable and predictable during both active and finished rounds
- theme toggle persists and stays readable in both themes
- mobile layout keeps the board square with no overflow
- keyboard focus states are visible and the `T` / `R` shortcuts behave sensibly

## Implementation intent
This ticket required a domain change rather than a refinement, so I performed a direct one-file replacement while keeping the repository's single-file app structure intact.
