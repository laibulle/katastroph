# Prime Numbers

Implement two functions:

```python
is_prime(n: int) -> bool
primes_up_to(limit: int) -> list[int]
```

`is_prime` checks one number. `primes_up_to` returns every prime number less than or
equal to `limit`.

Examples:

```python
is_prime(97) is True
primes_up_to(10) == [2, 3, 5, 7]
```

## Complexity Learning Goal

For `is_prime(n)`, checking divisors up to `sqrt(n)` gives `O(sqrt(n))` time.

For `primes_up_to(limit)`, the sieve is about `O(limit log log limit)`, which is much
better than testing every number independently for large limits.
