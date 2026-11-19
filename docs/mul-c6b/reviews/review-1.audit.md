# Audit: review-1.md
Plugin version: 0.0.0
Reviewed commit: 868c15ed44af762e6ba78d0af7ab64ded39e6b65

## Problems
- S1 `git diff --stat 996d9eaf7609adeb6ae57129608c76cd6a0b838b 868c15ed44af762e6ba78d0af7ab64ded39e6b65` rerun does not contain `5 files changed, 155 insertions(+)`

## Rerun log
C1 `python3 -m unittest tests.test_weather -v` expects `OK`: match
```
test_missing_key (tests.test_weather.Weather.test_missing_key) ... ok
test_request_shape (tests.test_weather.Weather.test_request_shape) ... ok
test_success (tests.test_weather.Weather.test_success) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK

[exit 0]
```

C1 `python3 -m unittest tests.test_weather -v` expects `test_request_shape (tests.test_weather.Weather`: match
```
test_missing_key (tests.test_weather.Weather.test_missing_key) ... ok
test_request_shape (tests.test_weather.Weather.test_request_shape) ... ok
test_success (tests.test_weather.Weather.test_success) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK

[exit 0]
```

C1 `weather.py:6` expects `SECRETS_PATH = Path(__file__).resolve().parent / "secrets.env"`: match
```
import urllib.request
from pathlib import Path

SECRETS_PATH = Path(__file__).resolve().parent / "secrets.env"


def _api_key():

```

C1 `weather.py:27` expects `f"https://api.example.com/weather?{query}"`: match
```
def fetch(city):
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )

```

C1 `weather.py:28` expects `headers={"X-API-Key": _api_key()},`: match
```
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:

```

C1 `weather.py:29` expects `method="GET",`: match
```
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

```

C1 `weather.py:31` expects `with urllib.request.urlopen(req, timeout=10) as resp:`: match
```
        headers={"X-API-Key": _api_key()},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

```

C1 `weather.py:32` expects `return json.loads(resp.read())`: match
```
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())

```

C1 `tests/test_weather.py:34` expects `self.assertEqual(req.full_url, "https://api.example.com/weather?city=San+Jos%C3%A9")`: match
```
            m.return_value.__enter__.return_value.read.return_value = b"{}"
            weather.fetch("San José")
        req = m.call_args.args[0]
        self.assertEqual(req.full_url, "https://api.example.com/weather?city=San+Jos%C3%A9")
        self.assertEqual(req.get_method(), "GET")
        self.assertEqual(req.get_header("X-api-key"), KEY)
        self.assertEqual(m.call_args.kwargs["timeout"], 10)

```

C1 `tests/test_weather.py:36` expects `self.assertEqual(req.get_header("X-api-key"), KEY)`: match
```
        req = m.call_args.args[0]
        self.assertEqual(req.full_url, "https://api.example.com/weather?city=San+Jos%C3%A9")
        self.assertEqual(req.get_method(), "GET")
        self.assertEqual(req.get_header("X-api-key"), KEY)
        self.assertEqual(m.call_args.kwargs["timeout"], 10)

    def test_missing_key(self):

```

C2 `tests/test_weather.py:18` expects `patcher = mock.patch.object(weather, "SECRETS_PATH", self.path)`: match
```
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.path = Path(tmp.name) / "keys.txt"
        patcher = mock.patch.object(weather, "SECRETS_PATH", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)


```

C2 `tests/test_weather.py:24` expects `with mock.patch("weather.urllib.request.urlopen") as m:`: match
```

    def test_success(self):
        self.path.write_text(f"WEATHER_API_KEY={KEY}\n", encoding="utf-8")
        with mock.patch("weather.urllib.request.urlopen") as m:
            m.return_value.__enter__.return_value.read.return_value = b'{"temp": 21}'
            self.assertEqual(weather.fetch("San José"), {"temp": 21})


```

C2 `tests/test_weather.py:30` expects `with mock.patch("weather.urllib.request.urlopen") as m:`: match
```

    def test_request_shape(self):
        self.path.write_text(f"# c\n\nWEATHER_API_KEY='{KEY}'\n", encoding="utf-8")
        with mock.patch("weather.urllib.request.urlopen") as m:
            m.return_value.__enter__.return_value.read.return_value = b"{}"
            weather.fetch("San José")
        req = m.call_args.args[0]

```

C2 `python3 -m unittest discover -s tests` expects `OK`: match
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK

[exit 0]
```

C2 `python3 -m unittest discover -s tests` expects `[exit 0]`: match
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.003s

OK

[exit 0]
```

C3 `.github/workflows/ci.yml:4` expects `pull_request:`: match
```
name: CI

on:
  pull_request:
  push:
    branches: [main]


```

C3 `.github/workflows/ci.yml:9` expects `contents: read`: match
```
    branches: [main]

permissions:
  contents: read

jobs:
  test:

```

C3 `.github/workflows/ci.yml:19` expects `- run: python3 -m unittest discover -s tests`: match
```
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: python3 -m unittest discover -s tests

```

C3 `grep -cE "secrets\.|deploy" .github/workflows/ci.yml` expects `[exit 1]`: match
```
0

[exit 1]
```

S1 `weather.py:21` expects `raise RuntimeError("WEATHER_API_KEY not found in secrets.env")`: match
```
                value = value[1:-1]
            if value:
                return value
    raise RuntimeError("WEATHER_API_KEY not found in secrets.env")


def fetch(city):

```

S1 `weather.py:25` expects `query = urllib.parse.urlencode({"city": city})`: match
```


def fetch(city):
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},

```

S1 `git diff --name-only 996d9eaf7609adeb6ae57129608c76cd6a0b838b 868c15ed44af762e6ba78d0af7ab64ded39e6b65 -- calc.py deploy.sh secrets.env .gitignore; echo "files-checked"` expects `files-checked`: match
```
files-checked
Traceback (most recent call last):
  File "/var/folders/fh/6chnhm7x76l6dbxgghp4qw2w0000gp/T/e2e-9hqju268/bin/git", line 149, in <module>
    shim(Path(sys.argv[0]).name)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/folders/fh/6chnhm7x76l6dbxgghp4qw2w0000gp/T/e2e-9hqju268/bin/git", line 124, in shim
    real = os.environ[f"AGENT_FLOW_REAL_{tool.upper()}"]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 709, in __getitem__
KeyError: 'AGENT_FLOW_REAL_GIT'

[exit 0]
```

S1 `git diff --stat 996d9eaf7609adeb6ae57129608c76cd6a0b838b 868c15ed44af762e6ba78d0af7ab64ded39e6b65` expects `5 files changed, 155 insertions(+)`: mismatch
```
Traceback (most recent call last):
  File "/var/folders/fh/6chnhm7x76l6dbxgghp4qw2w0000gp/T/e2e-9hqju268/bin/git", line 149, in <module>
    shim(Path(sys.argv[0]).name)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/folders/fh/6chnhm7x76l6dbxgghp4qw2w0000gp/T/e2e-9hqju268/bin/git", line 124, in shim
    real = os.environ[f"AGENT_FLOW_REAL_{tool.upper()}"]
           ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 709, in __getitem__
KeyError: 'AGENT_FLOW_REAL_GIT'

[exit 1]
```

Result: failed
