# Balanced Partition

Implement `balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]`.

Split the input into two groups such that the absolute difference between group sums is
as small as possible.

Example:

```python
left, right = balanced_partition([3, 1, 4, 2, 2])
abs(sum(left) - sum(right)) == 0
```

