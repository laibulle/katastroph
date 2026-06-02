# Recursion

Implement `factorial_recursive(n: int) -> int`.

Return `n!`, where:

```python
0! == 1
1! == 1
5! == 120
```

Raise `ValueError` for negative inputs.

## Complexity Learning Goal

Let `n` be the input number.

The recursive solution performs one call per integer from `n` down to `1`, so time is
`O(n)`. The call stack also grows to `O(n)`.
