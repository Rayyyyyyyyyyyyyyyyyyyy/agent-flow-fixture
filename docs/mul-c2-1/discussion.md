# mul-c2-1 - discussion

## Original words

> Implement the Goal in this repo's README.md. Use docs topic `mul-c2-1`.

README.md `## Goal`, quoted for reference:

> Add `mul(a, b)` to `calc.py` (returns the product) with a test.

(2026-11-19)

## Finish line

- C1 `calc.mul(a, b)` exists in `calc.py` and returns the product `a * b`, for ints, negatives, zero and floats. evidence: `python3 -c "import calc; print(calc.mul(6, 7), calc.mul(-2, 3), calc.mul(0, 5), calc.mul(2.5, 4))"` from the repo root -> prints `42 -6 0 10.0`
- C2 A unit test for `mul` is in `tests/test_calc.py` and the whole suite passes. evidence: `python3 -m unittest tests.test_calc -v` -> output contains `test_mul` with `ok`, and ends `OK`; `python3 -m unittest discover -s tests` -> `OK`
- C3 CI runs the suite on the PR and is green. evidence: `gh pr checks <n>` shows the `test` job passing

## Authorizations

> (none beyond invoking agent-flow on 2026-11-19)

## Decisions

- 2026-11-19 agent: classified as a goal (names file, function, behavior and test); no questions asked.
- 2026-11-19 agent: verify command is `python3 -m unittest discover -s tests` (README.md). CI already exists: `.github/workflows/ci.yml` runs exactly that on `pull_request` and on push to `main`; last `main` run is green. So there is no CI ticket.
- 2026-11-19 agent: branch protection on `main` is not set (API 404). Not adding it: this is a shared e2e fixture repo and a persistent settings change could affect other runs. `merge_gate.py` is the guard.
- 2026-11-19 agent: one ticket (01). The goal is a single verifiable behavior; splitting the function and its test would leave a ticket with nothing to verify.
- 2026-11-19 agent: `mul` matches the style of `add`/`sub`: plain `return a * b`, no type checks, no docstring. Python's own `*` semantics (e.g. `"a" * 3`) are left as is; restricting types is beyond the README's words.
- 2026-11-19 agent: README line "It deliberately has no CI" is stale since PR #3 added CI. Not changed here (outside this goal); option for the user.

## Open questions

- None.
