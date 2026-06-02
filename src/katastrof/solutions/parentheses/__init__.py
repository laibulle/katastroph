from functools import reduce


OPENING = {"(", "[", "{"}
PAIRS = {")": "(", "]": "[", "}": "{"}


def _consume_char(stack: list[str] | None, char: str) -> list[str] | None:
    if stack is None:
        return None
    if char in OPENING:
        stack.append(char)
        return stack
    if char not in PAIRS:
        return stack
    if not stack or stack[-1] != PAIRS[char]:
        return None
    stack.pop()
    return stack


def valid_parentheses(text: str) -> bool:
    return reduce(_consume_char, text, []) == []
