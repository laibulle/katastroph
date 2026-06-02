# Move Dots

Implement `move_dots_to_end(items: list[str]) -> list[str]`.

Move every `"."` to the end of the list while preserving the relative order of every
other value.

Example:

```python
move_dots_to_end(["a", "b", ".", "c", ".", ".", "k"])
```

returns `["a", "b", "c", "k", ".", ".", "."]`.

## Complexity Learning Goal

Let `n` be the list length.

Aim for `O(n)` time: inspect each item once. Space can be `O(n)` for a clear solution,
or `O(1)` extra space for an in-place variant.
