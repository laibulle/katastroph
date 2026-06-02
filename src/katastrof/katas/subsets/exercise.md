# Subsets

Implement `subsets(items: list[int]) -> list[list[int]]`.

Return every subset of the input. Ordering of subsets is not important.

Example:

```python
subsets([1, 2]) == [[], [1], [2], [1, 2]]
```

## Complexity Learning Goal

Let `n` be the number of items.

There are `2^n` subsets, so any complete solution is at least `O(2^n)` time and space.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_subsets.py
```
