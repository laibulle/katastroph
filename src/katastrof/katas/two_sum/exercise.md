# Two Sum

Implement `two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None`.

Return two values from the input whose sum equals `target`, or `None` if no such pair
exists.

Example:

```python
two_sum([10, 15, 3, 7], 17) == (10, 7)
```

## Complexity Learning Goal

Let `n` be the number of inputs.

The set-based solution is `O(n)` average time and `O(n)` space. The brute-force nested
loop solution is `O(n^2)`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_two_sum.py
```
