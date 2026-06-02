from typing import Iterable


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    seen = set()

    for n in numbers:
        complement = target - n
        if complement in seen:
            return complement, n

        seen.add(n)

    return None

