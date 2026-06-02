def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    return a if b == 0 else gcd(b, a % b)
