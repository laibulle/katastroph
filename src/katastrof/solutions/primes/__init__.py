from math import isqrt


def _odd_divisors_up_to(limit: int):
    return range(3, isqrt(limit) + 1, 2)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % divisor != 0 for divisor in _odd_divisors_up_to(n))


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (((limit - start) // candidate) + 1)
    return [
        number
        for number, prime in enumerate(sieve)
        if prime
    ]
