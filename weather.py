import json
import urllib.parse
import urllib.request
from pathlib import Path

SECRETS_PATH = Path(__file__).resolve().parent / "secrets.env"


def _api_key():
    for line in SECRETS_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        name, value = line.split("=", 1)
        if name.strip() == "WEATHER_API_KEY":
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            if value:
                return value
    raise RuntimeError("WEATHER_API_KEY not found in secrets.env")


def fetch(city):
    query = urllib.parse.urlencode({"city": city})
    req = urllib.request.Request(
        f"https://api.example.com/weather?{query}",
        headers={"X-API-Key": _api_key()},
        method="GET",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())
