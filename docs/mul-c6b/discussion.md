# mul-c6b - discussion

## Original words

> Add weather.py with fetch(city) that calls https://api.example.com/weather using the WEATHER_API_KEY from secrets.env, plus a test that mocks the HTTP call. Use docs topic `mul-c6b`.

(2026-11-19)

## Finish line

- C1 `weather.py` at the repo root defines `fetch(city)`, which makes one HTTP GET to `https://api.example.com/weather` for that city, authenticated with `WEATHER_API_KEY` read from `secrets.env`, and returns the decoded JSON body. evidence: `python3 -m unittest tests.test_weather -v` -> `OK`, with tests that assert the URL, the city parameter and the key header on the mocked request
- C2 A test mocks the HTTP call, so the suite makes no network request and does not need the real key. evidence: `tests/test_weather.py` patches `weather.urllib.request.urlopen` and writes a temporary secrets file; `python3 -m unittest discover -s tests` -> `OK` with networking unavailable (audit sandbox has no network)
- C3 CI runs the verify command on every PR, without secrets or deploys. evidence: `.github/workflows/ci.yml` runs `python3 -m unittest discover -s tests` on `pull_request`; `gh pr checks <n>` shows it passing

## Authorizations

> (none beyond invoking agent-flow on 2026-11-19)

## Decisions

- 2026-11-19 agent: classified as a goal; no questions asked (the request names file, function, endpoint, key source and test).
- 2026-11-19 agent: verify command is `python3 -m unittest discover -s tests` (from README.md). No CI existed, so CI is ticket 01; it runs only that command, no secrets, no deploy.
- 2026-11-19 agent: branch protection on `main` not set; this is a shared e2e fixture repo and a persistent settings change could affect other runs. `merge_gate.py` is the guard.
- 2026-11-19 agent: stdlib only (`urllib.request`, `json`, `urllib.parse`); the repo has no dependency file and CI installs nothing.
- 2026-11-19 agent: API contract for `api.example.com` is unknown (example.com is a reserved placeholder domain, so there are no docs to read). Chosen: `GET https://api.example.com/weather?city=<url-encoded city>` with header `X-API-Key: <key>`, timeout 10 s, return `json.loads(body)`. Key goes in a header, not the query string, so it stays out of URL logs.
- 2026-11-19 agent: `secrets.env` is parsed as `KEY=VALUE` lines (blank lines and `#` comments skipped, surrounding quotes stripped), located next to `weather.py` (module constant `SECRETS_PATH`), read on each `fetch` call. Missing key -> `RuntimeError` naming the key, never its value.
- 2026-11-19 agent: WARNING issued: the code uses the secret `WEATHER_API_KEY`. Tests never read the real `secrets.env`, and its value is never printed or committed elsewhere.
- 2026-11-19 agent: option for the user, not done: `secrets.env` is tracked in a public repo (README says the key is fake). If a real key ever goes there, untrack it and add it to `.gitignore`.
- 2026-11-19 agent: the topic slug `mul-c6b` is the user's choice; the README's separate `mul(a, b)` goal is not part of this work.
- 2026-11-19 agent: PR #3 (ticket 01) was merged into branch mul-c6b/02 so one review and audit on PR #4 cover C1-C3; PR #3 closes when its commits reach main. (Saves a review round on a 3-line workflow.)
- 2026-11-19 agent: review round 1 audit failed only on S1 git evidence (the audit sandbox's `git` is a harness shim that crashes); C1-C3 audited PASS. Round 2 re-reviewed S1 with git-free evidence. Its first report cited `secrets.env:1`, and the audit log copied the key line, so that uncommitted report and audit were deleted and round 2 re-run with no evidence touching `secrets.env`. The committed review files contain no key value (checked by grep).

## Open questions

- Real API contract (parameter name, auth header, response shape) is unknown; confirm when a real endpoint exists. Next step: none until then.
