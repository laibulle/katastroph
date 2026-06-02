# Greatest Common Divisor

Implement `gcd(a: int, b: int) -> int`.

Return the greatest common divisor using Euclid's algorithm.

Examples:

```python
gcd(54, 24) == 6
gcd(-54, 24) == 6
gcd(0, 5) == 5
```

## Complexity Learning Goal

Let `a` and `b` be the input values.

Euclid's algorithm is `O(log min(a, b))` because each modulo step shrinks the problem
quickly.
