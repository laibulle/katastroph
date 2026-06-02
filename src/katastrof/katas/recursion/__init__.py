def factorial_recursive(n: int) -> int:
    if n == 0:
        return 1

    return _factorial_recursive(n-1, n)

def _factorial_recursive(n: int, value: int) -> int:
    if n == 0:
        return value

    return _factorial_recursive(n - 1, value * n)