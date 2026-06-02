def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

