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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `fibonacci` kata.

Context:
- Exercise: `src/katastrof/katas/fibonacci/exercise.md`
- My solution: `src/katastrof/katas/fibonacci/__init__.py`
- Tests: `tests/test_fibonacci.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/fibonacci/__init__.py`
- Ideal explanation: `src/katastrof/solutions/fibonacci/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
