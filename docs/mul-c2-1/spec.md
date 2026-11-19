# mul-c2-1 - spec

## Problem

`calc.py` has `add` and `sub` but no multiplication. The README goal asks for `mul(a, b)` returning the product, with a test.

## Solution

Add `def mul(a, b): return a * b` to `calc.py`, after `sub`, in the same style. Add `test_mul` to the existing `Calc` test case in `tests/test_calc.py`.

## User stories

- As a user of `calc`, I call `calc.mul(6, 7)` and get `42`.

## Implementation decisions

- Plain `a * b`, no type checks (matches `add`/`sub`).
- No new files, no dependencies.

## Testing decisions

- `test_mul` asserts at least: `mul(6, 7) == 42`, `mul(-2, 3) == -6`, `mul(0, 5) == 0`, and a float case such as `mul(2.5, 4) == 10.0`.
- Verify: `python3 -m unittest discover -s tests` -> `OK`. CI runs the same command.

## Out of scope

- Changes to `add`, `sub`, `deploy.sh`, `secrets.env`, README. CI is added by its own ticket (02).
