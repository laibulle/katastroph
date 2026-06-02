from functools import reduce


def _next_pair(pair: tuple[int, int], _: int) -> tuple[int, int]:
    previous, current = pair
    return current, previous + current


def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci is undefined for negative integers")
    return reduce(_next_pair, range(n), (0, 1))[0]
