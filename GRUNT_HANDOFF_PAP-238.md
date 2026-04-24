# GRUNT HANDOFF — PAP-238

## What I changed
Applied a focused refinement pass to the existing single-file Tic Tac Toe app in `index.html`.

### UX / clarity updates
- renamed the ambiguous secondary control from `Clear board` to `Next round`
- clarified helper copy to explain keyboard shortcuts and restart behavior
- made the status badge more explicit during play and after wins:
  - `Turn: X` / `Turn: O`
  - `Winner: X` / `Winner: O`
  - `Draw`

### Behavior / reliability updates
- made `Restart game` always reset the board with **X** starting
- made `Next round` always begin a fresh round with the starter alternating between X and O
- added `roundStarter` state so round progression is deterministic and labels match behavior
- updated theme storage key to match this ticket (`pap-238-theme`)

## Files changed
- `index.html`

## Files added
- `GRUNT_HANDOFF_PAP-238.md`

## Validation performed
- JavaScript syntax check passed
- local HTTP smoke test passed
- confirmed the updated HTML contains the renamed next-round control and PAP-238 theme storage key

## Notes for Pedant
Please verify:
- `Restart game` always returns to an empty board with X starting
- `Next round` always clears the board and alternates the starting player
- status badge and status message always match the true state
- win/draw behavior is unchanged and still correct
- no moves are possible after game over until a reset action is used
- theme toggle and persistence still work as expected
- mobile layout remains square, balanced, and overflow-free

## Implementation intent
This was intentionally a minimal refinement, not a rewrite. The main goal was to remove ambiguity from reset behavior and make game state messaging more explicit.
