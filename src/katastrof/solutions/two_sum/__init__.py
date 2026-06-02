from typing import Iterable


def _match_or_remember(number: int, target: int, seen: set[int]) -> tuple[int, int] | None:
    complement = target - number
    if complement in seen:
        return complement, number
    seen.add(number)
    return None


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    seen: set[int] = set()
    for number in numbers:
        if match := _match_or_remember(number, target, seen):
            return match
    return None
