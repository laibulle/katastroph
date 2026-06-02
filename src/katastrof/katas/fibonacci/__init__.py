def fibonacci_iterative(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    i, i_1, i_2 = 2, 1, 0

    while i <= n:
        i_1, i_2 = i_2, i_1 + i_2
        i+=1

    return i_2 + i_1

