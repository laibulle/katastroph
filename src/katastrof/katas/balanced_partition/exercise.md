# Balanced Partition

Implement `balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]`.

Split the input into two groups such that the absolute difference between group sums is
as small as possible.

Example:

```python
left, right = balanced_partition([3, 1, 4, 2, 2])
abs(sum(left) - sum(right)) == 0
```

## Complexity Learning Goal

Let `n` be the number of values and `S` be their total sum.

An exact solution is usually pseudo-polynomial: `O(n * S)`. That means it depends on
the numeric values, not only on how many values there are.
