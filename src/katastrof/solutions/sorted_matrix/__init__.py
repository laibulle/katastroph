from heapq import heappop, heappush


def _initial_heap(matrix: list[list[int]]) -> list[tuple[int, int, int]]:
    return [
        (row[0], row_index, 0)
        for row_index, row in enumerate(matrix)
        if row
    ]


def _push_next_value(
    heap: list[tuple[int, int, int]],
    matrix: list[list[int]],
    row_index: int,
    col_index: int,
) -> None:
    next_col = col_index + 1
    if next_col < len(matrix[row_index]):
        heappush(heap, (matrix[row_index][next_col], row_index, next_col))


def merge_sorted_matrix(matrix: list[list[int]]) -> list[int]:
    """Return all values from a row/column sorted matrix in ascending order."""
    heap = _initial_heap(matrix)
    result: list[int] = []
    while heap:
        value, row_index, col_index = heappop(heap)
        result.append(value)
        _push_next_value(heap, matrix, row_index, col_index)
    return result
