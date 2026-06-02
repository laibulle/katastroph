# Merge Intervals

Implement `merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]`.

Each interval is `(start, end)`. Merge overlapping intervals and return the result
sorted by start.

Example:

```python
merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12)]) == [(1, 6), (8, 12)]
```

## Complexity Learning Goal

Let `n` be the number of intervals.

Sorting dominates the solution: `O(n log n)` time. The merge scan is `O(n)`. Space is
`O(n)` for the output.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_merge_intervals.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `merge_intervals` kata.

Context:
- Exercise: `src/katastrof/katas/merge_intervals/exercise.md`
- My solution: `src/katastrof/katas/merge_intervals/__init__.py`
- Tests: `tests/test_merge_intervals.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/merge_intervals/__init__.py`
- Ideal explanation: `src/katastrof/solutions/merge_intervals/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
