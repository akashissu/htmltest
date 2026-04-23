# GRUNT HANDOFF — PAP-231

## What I changed
- Refined the existing calculator implementation in `index.html` instead of replacing it wholesale.
- Kept the modern glassy calculator layout, responsive keypad, and dark-mode-aware styling.
- Improved interaction polish by adding stronger hover/active border and press feedback on calculator buttons.
- Strengthened JavaScript behavior for:
  - sanitized expression evaluation
  - clearer invalid-expression vs divide-by-zero error handling
  - live preview updates while typing valid expressions
  - better recovery after delete/clear/error states
  - safer keyboard handling that avoids intercepting modified shortcuts or editable fields

## Reliability notes
- Expressions are sanitized before evaluation.
- The calculator avoids evaluating incomplete inputs that end in an operator or decimal point.
- Non-finite results surface as a friendly divide-by-zero error.
- Invalid expressions surface as a distinct invalid-expression message.
- Delete now refreshes the preview/result instead of only echoing raw text.
- Keyboard shortcuts are ignored when modifier keys are pressed or focus is inside editable content.

## Suggested Pedant checks
- Verify live preview updates as numbers/operators are entered.
- Verify `=` still evaluates correctly for `+`, `-`, `*`, and `/`.
- Verify `AC`, `DEL`, and post-error recovery behave correctly.
- Verify invalid expressions show `Invalid expression` and divide-by-zero shows `Cannot divide by zero`.
- Verify hover, focus-visible, and active states remain polished in both light and dark modes.
- Verify keyboard input works without interfering with browser/system shortcuts.

## Files changed
- `index.html`
- `GRUNT_HANDOFF_PAP-231.md`
