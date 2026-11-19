import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import weather

KEY = "test-key-123"


class Weather(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.path = Path(tmp.name) / "keys.txt"
        patcher = mock.patch.object(weather, "SECRETS_PATH", self.path)
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_success(self):
        self.path.write_text(f"WEATHER_API_KEY={KEY}\n", encoding="utf-8")
        with mock.patch("weather.urllib.request.urlopen") as m:
            m.return_value.__enter__.return_value.read.return_value = b'{"temp": 21}'
            self.assertEqual(weather.fetch("San José"), {"temp": 21})

    def test_request_shape(self):
        self.path.write_text(f"# c\n\nWEATHER_API_KEY='{KEY}'\n", encoding="utf-8")
        with mock.patch("weather.urllib.request.urlopen") as m:
            m.return_value.__enter__.return_value.read.return_value = b"{}"
            weather.fetch("San José")
        req = m.call_args.args[0]
        self.assertEqual(req.full_url, "https://api.example.com/weather?city=San+Jos%C3%A9")
        self.assertEqual(req.get_method(), "GET")
        self.assertEqual(req.get_header("X-api-key"), KEY)
        self.assertEqual(m.call_args.kwargs["timeout"], 10)

    def test_missing_key(self):
        self.path.write_text("OTHER=secretvalue\n", encoding="utf-8")
        with self.assertRaises(RuntimeError) as cm:
            weather.fetch("x")
        self.assertIn("WEATHER_API_KEY", str(cm.exception))
        self.assertNotIn("secretvalue", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
