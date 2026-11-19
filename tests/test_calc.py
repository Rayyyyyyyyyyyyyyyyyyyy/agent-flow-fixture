import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import calc


class Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(6, 7), 42)
        self.assertEqual(calc.mul(-2, 3), -6)
        self.assertEqual(calc.mul(0, 5), 0)
        self.assertEqual(calc.mul(2.5, 4), 10.0)


if __name__ == "__main__":
    unittest.main()
