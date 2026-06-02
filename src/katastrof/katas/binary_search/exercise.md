# Binary Search

Implement `binary_search(sorted_items: list[int], target: int) -> int`.

Return the index of `target` in a sorted list, or `-1` when absent.

Examples:

```python
binary_search([1, 3, 5, 7], 5) == 2
binary_search([1, 3, 5, 7], 2) == -1
```

## Complexity Learning Goal

Let `n` be the list length.

Binary search is `O(log n)` because each comparison cuts the remaining search interval
roughly in half.
