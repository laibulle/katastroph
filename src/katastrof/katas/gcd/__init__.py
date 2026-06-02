def gcd(a: int, b: int) -> int:
    divider = find_first_divider_try(a, b)



    if a == 0:
        return b
    if b == 0:
        return a

    if divider == 0:
        return -1

    while not is_divided(a, divider) or not is_divided(b, divider):
        divider-=1

        if divider == 0:
            return -1


    return divider

def find_first_divider_try(a: int, b: int) -> int:
    abs_a, abs_b = abs(a), abs(b)
    if abs_a == 0 or abs_b == 0:
        return 0

    if abs_a < abs_b:
        return abs_a

    return abs_b

def is_divided(a: int, b: int) -> bool:
    return a % b == 0