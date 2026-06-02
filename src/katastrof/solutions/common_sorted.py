def common_sorted(left: list[str], right: list[str]) -> list[str]:
    """Return common items from two sorted lists, preserving duplicate counts."""
    i = j = 0
    result: list[str] = []
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            result.append(left[i])
            i += 1
            j += 1
        elif left[i] < right[j]:
            i += 1
        else:
            j += 1
    return result

