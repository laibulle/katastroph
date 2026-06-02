def binary_search(sorted_items: list[int], target: int) -> int:
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

