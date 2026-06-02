# Recursion

Implement `factorial_recursive(n: int) -> int`.

Return `n!`, where:

```python
0! == 1
1! == 1
5! == 120
```

Raise `ValueError` for negative inputs.

## Complexity Learning Goal

Let `n` be the input number.

The recursive solution performs one call per integer from `n` down to `1`, so time is
`O(n)`. The call stack also grows to `O(n)`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_recursion.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `recursion` kata.

Context:
- Exercise: `src/katastrof/katas/recursion/exercise.md`
- My solution: `src/katastrof/katas/recursion/__init__.py`
- Tests: `tests/test_recursion.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/recursion/__init__.py`
- Ideal explanation: `src/katastrof/solutions/recursion/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
