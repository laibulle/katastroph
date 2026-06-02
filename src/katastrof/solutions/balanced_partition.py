def balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Split numbers into two groups with the smallest possible sum difference."""
    total = sum(numbers)
    reachable: dict[int, int] = {0: -1}
    for index, value in enumerate(numbers):
        for subtotal in list(reachable):
            new_total = subtotal + value
            if new_total not in reachable:
                reachable[new_total] = index

    target = min(reachable, key=lambda subtotal: abs(total - 2 * subtotal))
    chosen_indices: set[int] = set()
    subtotal = target
    for index in range(len(numbers) - 1, -1, -1):
        value = numbers[index]
        if subtotal - value in reachable and reachable[subtotal] == index:
            chosen_indices.add(index)
            subtotal -= value

    left = [value for index, value in enumerate(numbers) if index in chosen_indices]
    right = [value for index, value in enumerate(numbers) if index not in chosen_indices]
    return left, right

