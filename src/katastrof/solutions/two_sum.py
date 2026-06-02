from typing import Iterable


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    seen: set[int] = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return complement, number
        seen.add(number)
    return None

