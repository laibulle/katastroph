def fibonacci_iterative(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    i = 2
    i_1 = 1
    i_2 = 0

    while i <= n:
        t_1 = i_1 + i_2
        i_1 = i_2
        i_2 = t_1
        i+=1

    return i_2 + i_1

