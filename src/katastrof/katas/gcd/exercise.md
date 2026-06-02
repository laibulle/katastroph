# Greatest Common Divisor

Implement `gcd(a: int, b: int) -> int`.

Return the greatest common divisor using Euclid's algorithm.

Examples:

```python
gcd(54, 24) == 6
gcd(-54, 24) == 6
gcd(0, 5) == 5
```

## Complexity Learning Goal

Let `a` and `b` be the input values.

Euclid's algorithm is `O(log min(a, b))` because each modulo step shrinks the problem
quickly.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_gcd.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `gcd` kata.

Context:
- Exercise: `src/katastrof/katas/gcd/exercise.md`
- My solution: `src/katastrof/katas/gcd/__init__.py`
- Tests: `tests/test_gcd.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/gcd/__init__.py`
- Ideal explanation: `src/katastrof/solutions/gcd/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
