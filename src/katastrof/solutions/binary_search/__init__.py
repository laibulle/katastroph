def _search_between(sorted_items: list[int], target: int, low: int, high: int) -> int:
    if low > high:
        return -1

    middle = (low + high) // 2
    value = sorted_items[middle]

    if value == target:
        return middle
    if value < target:
        return _search_between(sorted_items, target, middle + 1, high)
    return _search_between(sorted_items, target, low, middle - 1)


def binary_search(sorted_items: list[int], target: int) -> int:
    return _search_between(sorted_items, target, 0, len(sorted_items) - 1)
