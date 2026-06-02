from typing import Iterable


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    i = 0
    last_idx_to_test = len(numbers) - 1

    while i < last_idx_to_test:
        for op2 in numbers[i+1::]:
            res = equals_target(numbers[i], op2, target)
            if res is not None:
                return res
        i += 1
    return None


def equals_target(op1, op2, target) -> tuple[int, int] | None:
    if op1 + op2 == target:
        return (op1, op2)
    else:
        None
