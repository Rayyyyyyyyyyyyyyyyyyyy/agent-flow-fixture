# Review: mul-c2-1 round 1

Reviewer model: claude-opus-5-5
Reviewed commit: 5bdafe9a0798bb876984c0154540c3a8b9b83a90
Base: 996d9eaf7609adeb6ae57129608c76cd6a0b838b

### C1 — PASS
Criterion: `calc.mul(a, b)` exists in `calc.py` and returns the product `a * b`, for ints, negatives, zero and floats.
Command: `python3 -c "import calc; print(calc.mul(6, 7), calc.mul(-2, 3), calc.mul(0, 5), calc.mul(2.5, 4))"`
Output contains: `42 -6 0 10.0`
Position: `calc.py:9`
Contains: `def mul(a, b):`
Position: `calc.py:10`
Contains: `return a * b`

### C2 — PASS
Criterion: A unit test for `mul` is in `tests/test_calc.py` and the whole suite passes.
Position: `tests/test_calc.py:16`
Contains: `def test_mul(self):`
Position: `tests/test_calc.py:20`
Contains: `self.assertEqual(calc.mul(2.5, 4), 10.0)`
Command: `python3 -m unittest tests.test_calc -v`
Output contains: `test_mul`
Command: `python3 -m unittest tests.test_calc -v`
Output contains: `[exit 0]`
Command: `python3 -m unittest discover -s tests`
Output contains: `OK`
Command: `python3 -m unittest discover -s tests`
Output contains: `[exit 0]`

### C3 — PASS
Criterion: CI runs the suite on every PR, without secrets or deploys, and is green on the PR.
Position: `.github/workflows/ci.yml:3`
Contains: `pull_request:`
Position: `.github/workflows/ci.yml:5`
Contains: `branches: [main]`
Position: `.github/workflows/ci.yml:9`
Contains: `test:`
Position: `.github/workflows/ci.yml:16`
Contains: `run: python3 -m unittest discover -s tests`
Command: `grep -ciE "secret|deploy" .github/workflows/ci.yml`
Output contains: `[exit 1]`

The workflow has 16 lines, has `permissions: contents: read`, and does not mention a secret or `deploy.sh`. I could not check that CI is green on PR #6 offline. The main session reported that run 44483865899 passed the `test` job, and `scripts/merge_gate.py` requires a green CI before merge.

### C4 — PASS
Criterion: No code problem changes behavior in the diff 996d9ea..5bdafe9 (calc.py, tests/test_calc.py, .github/workflows/ci.yml). It must match the spec's Implementation decisions: plain `a * b`, no type checks, no new dependencies, `add`/`sub` unchanged, and no changes to `deploy.sh`, `secrets.env` or README.
Position: `calc.py:2`
Contains: `return a + b`
Position: `calc.py:6`
Contains: `return a - b`
Position: `tests/test_calc.py:11`
Contains: `self.assertEqual(calc.add(2, 3), 5)`
Position: `tests/test_calc.py:14`
Contains: `self.assertEqual(calc.sub(5, 3), 2)`

The diff adds lines only. No existing test was weakened, and no sleeps or swallowed errors were added. `.github/workflows/ci.yml` is outside the spec's ticket 01 scope ("CI is added by its own ticket (02)"). The discussion's Decisions record that PR #8 (ticket 02) was merged into this branch so that one review covers C1-C3. Finish-line item C3 needs it, so it is not a scope FAIL.

## Findings outside the criteria

- README still says the repo "deliberately has no CI". This is stale now that CI is added. The discussion records it as an option for the user, and it does not block the merge.
