# Fibonacci

Implement `fibonacci_iterative(n: int) -> int`.

Return the nth Fibonacci number with:

```python
fibonacci_iterative(0) == 0
fibonacci_iterative(1) == 1
```

Raise `ValueError` for negative inputs. Prefer iteration over recursion.

## Complexity Learning Goal

Let `n` be the requested index.

The target solution is `O(n)` time and `O(1)` space. Naive recursion is much worse
because it recomputes the same Fibonacci values many times.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_fibonacci.py
```
