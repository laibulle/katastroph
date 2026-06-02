def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci is undefined for negative integers")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

