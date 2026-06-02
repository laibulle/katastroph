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

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_primes.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `primes` kata.

Context:
- Exercise: `src/katastrof/katas/primes/exercise.md`
- My solution: `src/katastrof/katas/primes/__init__.py`
- Tests: `tests/test_primes.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/primes/__init__.py`
- Ideal explanation: `src/katastrof/solutions/primes/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
