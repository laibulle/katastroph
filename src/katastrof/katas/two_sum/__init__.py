from typing import Iterable


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    i = 0
    last_idx_to_test = len(numbers) - 1

    while i < last_idx_to_test:
        for op2 in numbers[i+1::]:
            if (numbers[i] + op2) == target:
                return (numbers[i], op2)
        i += 1
    return None
