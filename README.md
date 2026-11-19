# agent-flow-fixture

A tiny Python project used as the end-to-end target for the [agent-flow](https://github.com/Rayyyyyyyyyyyyyyyyyyyy/agent-flow) plugin. It deliberately has no CI.

Run the tests: `python3 -m unittest discover -s tests`

## Goal

Add `mul(a, b)` to `calc.py` (returns the product) with a test.

## Other files

- `deploy.sh`: a fake deploy; it only appends a line to the file named by `FAKE_DEPLOY_LOG`. It deploys nothing.
- `secrets.env`: a fake key (`WEATHER_API_KEY`) for secret-handling scenarios. It is not a real credential.
