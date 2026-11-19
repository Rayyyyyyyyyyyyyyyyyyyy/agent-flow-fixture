# Audit: review-1.md
Plugin version: 0.0.0
Reviewed commit: 5bdafe9a0798bb876984c0154540c3a8b9b83a90

## Problems
- none

## Rerun log
C1 `python3 -c "import calc; print(calc.mul(6, 7), calc.mul(-2, 3), calc.mul(0, 5), calc.mul(2.5, 4))"` expects `42 -6 0 10.0`: match
```
42 -6 0 10.0

[exit 0]
```

C1 `calc.py:9` expects `def mul(a, b):`: match
```
    return a - b


def mul(a, b):
    return a * b

```

C1 `calc.py:10` expects `return a * b`: match
```


def mul(a, b):
    return a * b

```

C2 `tests/test_calc.py:16` expects `def test_mul(self):`: match
```
    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(6, 7), 42)
        self.assertEqual(calc.mul(-2, 3), -6)
        self.assertEqual(calc.mul(0, 5), 0)

```

C2 `tests/test_calc.py:20` expects `self.assertEqual(calc.mul(2.5, 4), 10.0)`: match
```
        self.assertEqual(calc.mul(6, 7), 42)
        self.assertEqual(calc.mul(-2, 3), -6)
        self.assertEqual(calc.mul(0, 5), 0)
        self.assertEqual(calc.mul(2.5, 4), 10.0)


if __name__ == "__main__":

```

C2 `python3 -m unittest tests.test_calc -v` expects `test_mul`: match
```
test_add (tests.test_calc.Calc.test_add) ... ok
test_mul (tests.test_calc.Calc.test_mul) ... ok
test_sub (tests.test_calc.Calc.test_sub) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

[exit 0]
```

C2 `python3 -m unittest tests.test_calc -v` expects `[exit 0]`: match
```
test_add (tests.test_calc.Calc.test_add) ... ok
test_mul (tests.test_calc.Calc.test_mul) ... ok
test_sub (tests.test_calc.Calc.test_sub) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

[exit 0]
```

C2 `python3 -m unittest discover -s tests` expects `OK`: match
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

[exit 0]
```

C2 `python3 -m unittest discover -s tests` expects `[exit 0]`: match
```
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

[exit 0]
```

C3 `.github/workflows/ci.yml:3` expects `pull_request:`: match
```
name: CI
on:
  pull_request:
  push:
    branches: [main]
permissions:

```

C3 `.github/workflows/ci.yml:5` expects `branches: [main]`: match
```
on:
  pull_request:
  push:
    branches: [main]
permissions:
  contents: read
jobs:

```

C3 `.github/workflows/ci.yml:9` expects `test:`: match
```
permissions:
  contents: read
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

```

C3 `.github/workflows/ci.yml:16` expects `run: python3 -m unittest discover -s tests`: match
```
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: python3 -m unittest discover -s tests

```

C3 `grep -ciE "secret|deploy" .github/workflows/ci.yml` expects `[exit 1]`: match
```
0

[exit 1]
```

C4 `calc.py:2` expects `return a + b`: match
```
def add(a, b):
    return a + b


def sub(a, b):

```

C4 `calc.py:6` expects `return a - b`: match
```


def sub(a, b):
    return a - b


def mul(a, b):

```

C4 `tests/test_calc.py:11` expects `self.assertEqual(calc.add(2, 3), 5)`: match
```

class Calc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

```

C4 `tests/test_calc.py:14` expects `self.assertEqual(calc.sub(5, 3), 2)`: match
```
        self.assertEqual(calc.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(calc.sub(5, 3), 2)

    def test_mul(self):
        self.assertEqual(calc.mul(6, 7), 42)

```

Result: passed
