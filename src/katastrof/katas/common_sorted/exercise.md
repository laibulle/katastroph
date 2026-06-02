# Common Sorted

Implement `common_sorted(left: list[str], right: list[str]) -> list[str]`.

Both input lists are sorted. Return the common values while preserving duplicate counts.

Example:

```python
common_sorted(["a", "e", "e", "e"], ["b", "b", "c", "e", "e", "g"]) == ["e", "e"]
```

## Complexity Learning Goal

Let `n` and `m` be the input lengths.

Aim for work proportional to both inputs: `O(n + m)`. Avoid checking every item from
the first list against every item from the second list, which would be `O(n * m)`.
