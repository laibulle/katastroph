def binary_search(sorted_items: list[int], target: int) -> int:
    low = 0
    high = len(sorted_items) - 1

    while low <= high:
        mid = (low + high) // 2
        value = sorted_items[mid]

        if value == target:
            return mid
        elif value < target:
            low = mid + 1
            high = high
        elif value > target:
            high = mid - 1
            low = low

    return -1