from functools import reduce


def _merge_one(merged: list[tuple[int, int]], interval: tuple[int, int]) -> list[tuple[int, int]]:
    if not merged or interval[0] > merged[-1][1]:
        merged.append(interval)
        return merged

    start, end = merged[-1]
    merged[-1] = (start, max(end, interval[1]))
    return merged


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return reduce(_merge_one, sorted(intervals), [])

