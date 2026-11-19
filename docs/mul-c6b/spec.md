# mul-c6b - spec

## Problem
The project needs a function to fetch weather for a city from `https://api.example.com/weather`, authenticated with `WEATHER_API_KEY` from `secrets.env`, testable without the network. The repo has no CI.

## Solution
- `.github/workflows/ci.yml`: on `pull_request` and push to `main`, run `python3 -m unittest discover -s tests`.
- `weather.py` (repo root): `SECRETS_PATH = Path(__file__).resolve().parent / "secrets.env"`; `fetch(city)` reads the key, sends `GET https://api.example.com/weather?city=<urlencoded>` with header `X-API-Key`, timeout 10, returns `json.loads` of the body.
- `tests/test_weather.py`: patches `weather.urllib.request.urlopen` and `weather.SECRETS_PATH` (temporary file), asserts request URL, header, timeout, return value, and the missing-key error.

## User stories
- As a developer I call `weather.fetch("Paris")` and get the API's JSON as a dict.
- As a developer I run the tests offline and they pass.

## Implementation decisions
See Decisions in `discussion.md`. Stdlib only. Errors from `urlopen` propagate unchanged.

## Testing decisions
unittest + unittest.mock, no network, no real key.

## Out of scope
Retries, caching, response validation, a CLI, changes to `calc.py`, `deploy.sh`, `secrets.env`, `.gitignore`.
