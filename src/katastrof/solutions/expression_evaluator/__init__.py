def evaluate(expression: str) -> int:
    total = 0
    sign = 1
    number = 0
    stack: list[tuple[int, int]] = []

    for char in expression:
        if char.isdigit():
            number = number * 10 + int(char)
        elif char in "+-":
            total += sign * number
            number = 0
            sign = 1 if char == "+" else -1
        elif char == "(":
            stack.append((total, sign))
            total = 0
            sign = 1
        elif char == ")":
            total += sign * number
            previous_total, previous_sign = stack.pop()
            total = previous_total + previous_sign * total
            number = 0

    return total + sign * number

