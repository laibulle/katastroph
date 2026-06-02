from itertools import accumulate


def max_sum_subarray(numbers: list[int], size: int) -> int:
    if size <= 0 or size > len(numbers):
        raise ValueError("size must be between 1 and len(numbers)")

    prefix = [0, *accumulate(numbers)]
    window_sums = (
        prefix[end] - prefix[end - size]
        for end in range(size, len(prefix))
    )
    return max(window_sums)

