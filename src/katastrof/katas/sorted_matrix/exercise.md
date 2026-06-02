# Sorted Matrix

Implement `merge_sorted_matrix(matrix: list[list[int]]) -> list[int]`.

Each row and each column are sorted in ascending order. Return all values in ascending
order.

Example:

```python
merge_sorted_matrix([[1, 5, 9], [2, 6, 10], [3, 7, 11]])
```

returns `[1, 2, 3, 5, 6, 7, 9, 10, 11]`.

## Complexity Learning Goal

Let `N` be the total number of values and `r` be the number of rows.

A heap-based merge should be `O(N log r)`: every value is popped once, and heap
operations cost `log r`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_sorted_matrix.py
```
