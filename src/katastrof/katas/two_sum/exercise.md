# Two Sum

Implement `two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None`.

Return two values from the input whose sum equals `target`, or `None` if no such pair
exists.

Example:

```python
two_sum([10, 15, 3, 7], 17) == (10, 7)
```

## Complexity Learning Goal

Let `n` be the number of inputs.

The set-based solution is `O(n)` average time and `O(n)` space. The brute-force nested
loop solution is `O(n^2)`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_two_sum.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `two_sum` kata.

Context:
- Exercise: `src/katastrof/katas/two_sum/exercise.md`
- My solution: `src/katastrof/katas/two_sum/__init__.py`
- Tests: `tests/test_two_sum.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/two_sum/__init__.py`
- Ideal explanation: `src/katastrof/solutions/two_sum/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
