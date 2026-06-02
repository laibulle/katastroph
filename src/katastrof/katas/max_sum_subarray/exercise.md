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
