from collections import Counter


def common_sorted(left: list[str], right: list[str]) -> list[str]:
    """Return common items from two sorted lists, preserving duplicate counts."""
    common_counts = Counter(left) & Counter(right)
    return list(common_counts.elements())
