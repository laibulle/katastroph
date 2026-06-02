# Max Sum Subarray

Implement `max_sum_subarray(numbers: list[int], size: int) -> int`.

Return the maximum sum of any contiguous subarray of length `size`.

Example:

```python
max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
```

## Complexity Learning Goal

Let `n` be the number of values.

The sliding-window target is `O(n)` time: update the previous window sum instead of
re-summing each window from scratch.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_max_sum_subarray.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `max_sum_subarray` kata.

Context:
- Exercise: `src/katastrof/katas/max_sum_subarray/exercise.md`
- My solution: `src/katastrof/katas/max_sum_subarray/__init__.py`
- Tests: `tests/test_max_sum_subarray.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/max_sum_subarray/__init__.py`
- Ideal explanation: `src/katastrof/solutions/max_sum_subarray/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
