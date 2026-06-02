from functools import reduce


def _add_reachable_subtotals(
    reachable: dict[int, int],
    indexed_value: tuple[int, int],
) -> dict[int, int]:
    index, value = indexed_value
    additions = {
        subtotal + value: index
        for subtotal in reachable
        if subtotal + value not in reachable
    }
    reachable.update(additions)
    return reachable


def _best_subtotal(reachable: dict[int, int], total: int) -> int:
    return min(reachable, key=lambda subtotal: abs(total - 2 * subtotal))


def _chosen_indices(numbers: list[int], reachable: dict[int, int], target: int) -> set[int]:
    chosen: set[int] = set()
    subtotal = target
    for index, value in reversed(list(enumerate(numbers))):
        if subtotal - value in reachable and reachable[subtotal] == index:
            chosen.add(index)
            subtotal -= value
    return chosen


def _partition_by_indices(numbers: list[int], indices: set[int]) -> tuple[list[int], list[int]]:
    return (
        [value for index, value in enumerate(numbers) if index in indices],
        [value for index, value in enumerate(numbers) if index not in indices],
    )


def balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Split numbers into two groups with the smallest possible sum difference."""
    total = sum(numbers)
    reachable = reduce(_add_reachable_subtotals, enumerate(numbers), {0: -1})
    target = _best_subtotal(reachable, total)
    return _partition_by_indices(numbers, _chosen_indices(numbers, reachable, target))
