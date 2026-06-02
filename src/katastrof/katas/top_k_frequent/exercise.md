# Top K Frequent

Implement `top_k_frequent(items: list[str], k: int) -> list[str]`.

Return the `k` most frequent values. Ties should be ordered alphabetically.

Example:

```python
top_k_frequent(["b", "a", "b", "c", "a", "b"], 2) == ["b", "a"]
```

## Complexity Learning Goal

Let `n` be the number of items and `u` the number of unique values.

Counting is `O(n)`. Sorting unique values is `O(u log u)`.

