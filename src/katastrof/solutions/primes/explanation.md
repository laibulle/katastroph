# Prime Numbers Solution

`is_prime` handles small cases, rejects even numbers, then uses `all(...)` over odd
divisors up to `sqrt(n)`.

`primes_up_to` uses the Sieve of Eratosthenes. Composite numbers are marked starting at
`candidate * candidate`, because smaller multiples were already handled.

Complexity: `is_prime` is `O(sqrt(n))`; the sieve is about `O(n log log n)`.
