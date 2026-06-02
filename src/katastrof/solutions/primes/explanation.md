# Prime Numbers Solution

`is_prime` handles small cases, rejects even numbers, then uses `all(...)` over odd
divisors up to `sqrt(n)`.

`primes_up_to` uses the Sieve of Eratosthenes. Composite numbers are marked starting at
`candidate * candidate`, because smaller multiples were already handled.

Schema:

```text
2: mark 4, 6, 8, 10, ...
3: mark 9, 12, 15, ...
5: start at 25, because 10, 15, 20 were already marked
```

Complexity: `is_prime` is `O(sqrt(n))`; the sieve is about `O(n log log n)`.
