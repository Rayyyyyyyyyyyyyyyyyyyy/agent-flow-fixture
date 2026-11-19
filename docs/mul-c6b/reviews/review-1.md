# Review: mul-c6b round 1

Reviewer model: claude-opus-5-5
Reviewed commit: 868c15ed44af762e6ba78d0af7ab64ded39e6b65
Base: 996d9eaf7609adeb6ae57129608c76cd6a0b838b

### C1 — PASS
Criterion: `weather.py` at the repo root defines `fetch(city)`, which makes one HTTP GET to `https://api.example.com/weather` for that city, authenticated with `WEATHER_API_KEY` read from `secrets.env`, and returns the decoded JSON body; tests assert the URL, the city parameter and the key header on the mocked request.
Command: `python3 -m unittest tests.test_weather -v`
Output contains: `OK`
Command: `python3 -m unittest tests.test_weather -v`
Output contains: `test_request_shape (tests.test_weather.Weather`
Position: `weather.py:6`
Contains: `SECRETS_PATH = Path(__file__).resolve().parent / "secrets.env"`
Position: `weather.py:27`
Contains: `f"https://api.example.com/weather?{query}"`
Position: `weather.py:28`
Contains: `headers={"X-API-Key": _api_key()},`
Position: `weather.py:29`
Contains: `method="GET",`
Position: `weather.py:31`
Contains: `with urllib.request.urlopen(req, timeout=10) as resp:`
Position: `weather.py:32`
Contains: `return json.loads(resp.read())`
Position: `tests/test_weather.py:34`
Contains: `self.assertEqual(req.full_url, "https://api.example.com/weather?city=San+Jos%C3%A9")`
Position: `tests/test_weather.py:36`
Contains: `self.assertEqual(req.get_header("X-api-key"), KEY)`

### C2 — PASS
Criterion: A test mocks the HTTP call, so the suite makes no network request and does not need the real key.
Position: `tests/test_weather.py:18`
Contains: `patcher = mock.patch.object(weather, "SECRETS_PATH", self.path)`
Position: `tests/test_weather.py:24`
Contains: `with mock.patch("weather.urllib.request.urlopen") as m:`
Position: `tests/test_weather.py:30`
Contains: `with mock.patch("weather.urllib.request.urlopen") as m:`
Command: `python3 -m unittest discover -s tests`
Output contains: `OK`
Command: `python3 -m unittest discover -s tests`
Output contains: `[exit 0]`

### C3 — PASS
Criterion: CI runs the verify command on every PR, without secrets or deploys. (Pass status of the run itself needs the network; the gate reported `gh pr checks 3` -> test pass. Evidence here is the workflow file.)
Position: `.github/workflows/ci.yml:4`
Contains: `pull_request:`
Position: `.github/workflows/ci.yml:9`
Contains: `contents: read`
Position: `.github/workflows/ci.yml:19`
Contains: `- run: python3 -m unittest discover -s tests`
Command: `grep -cE "secrets\.|deploy" .github/workflows/ci.yml`
Output contains: `[exit 1]`

### S1 — PASS
Criterion: Security and scope range checked: whole diff 996d9ea..868c15e (ci.yml, weather.py, tests/test_weather.py, docs). The key is sent only in a header, never in the URL; the missing-key error names the key but not any value; no existing test, `calc.py`, `deploy.sh`, `secrets.env` or `.gitignore` was changed (spec Out of scope).
Position: `weather.py:21`
Contains: `raise RuntimeError("WEATHER_API_KEY not found in secrets.env")`
Position: `weather.py:25`
Contains: `query = urllib.parse.urlencode({"city": city})`
Command: `git diff --name-only 996d9eaf7609adeb6ae57129608c76cd6a0b838b 868c15ed44af762e6ba78d0af7ab64ded39e6b65 -- calc.py deploy.sh secrets.env .gitignore; echo "files-checked"`
Output contains: `files-checked`
Command: `git diff --stat 996d9eaf7609adeb6ae57129608c76cd6a0b838b 868c15ed44af762e6ba78d0af7ab64ded39e6b65`
Output contains: `5 files changed, 155 insertions(+)`

## Findings outside the items

- `secrets.env` is tracked in git and not in `.gitignore` (pre-existing at base; out of scope per spec, already recorded as a user option in discussion.md Decisions). Its value was not read or copied in this review.
- The tests do not assert `urlopen` is called exactly once; the code makes a single call (`weather.py:31`), so "one HTTP GET" holds by reading the code, not by a test assertion.
