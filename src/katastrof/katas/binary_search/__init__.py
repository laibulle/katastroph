def binary_search(sorted_items: list[int], target: int) -> int:
    for idx, item in enumerate(sorted_items):
        print(idx, item)
        if item == target:
            return idx
        elif target < item:
            return -1

    return -1
