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
