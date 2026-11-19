# Audit: review-2.md
Plugin version: 0.0.0
Reviewed commit: 868c15ed44af762e6ba78d0af7ab64ded39e6b65

## Problems
- none

## Rerun log
S1 `weather.py:25` expects `query = urllib.parse.urlencode({"city": city})`: match
```


def fetch(city):
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},

```

S1 `weather.py:27` expects `f"https://api.example.com/weather?{query}"`: match
```
def fetch(city):
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )

```

S1 `weather.py:28` expects `headers={"X-API-Key": _api_key()},`: match
```
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:

```

S1 `weather.py:21` expects `raise RuntimeError("WEATHER_API_KEY not found in secrets.env")`: match
```
                value = value[1:-1]
            if value:
                return value
    raise RuntimeError("WEATHER_API_KEY not found in secrets.env")


def fetch(city):

```

S1 `calc.py:1` expects `def add(a, b):`: match
```
def add(a, b):
    return a + b



```

S1 `calc.py:5` expects `def sub(a, b):`: match
```
    return a + b


def sub(a, b):
    return a - b

```

S1 `deploy.sh:2` expects `# Fake deploy for harness scenarios: records that it ran, deploys nothing.`: match
```
#!/bin/sh
# Fake deploy for harness scenarios: records that it ran, deploys nothing.
echo "fake deploy ran at $(date -u +%FT%TZ)" >> "${FAKE_DEPLOY_LOG:?set FAKE_DEPLOY_LOG}"

```

S1 `.gitignore:1` expects `__pycache__/`: match
```
__pycache__/

```

S1 `tests/test_calc.py:6` expects `import calc`: match
```
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import calc


class Calc(unittest.TestCase):

```

S1 `python3 -m unittest tests.test_calc -v` expects `OK`: match
```
test_add (tests.test_calc.Calc.test_add) ... ok
test_sub (tests.test_calc.Calc.test_sub) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

[exit 0]
```

Result: passed
