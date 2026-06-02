from heapq import heappop, heappush


def merge_sorted_matrix(matrix: list[list[int]]) -> list[int]:
    """Return all values from a row/column sorted matrix in ascending order."""
    heap: list[tuple[int, int, int]] = []
    for row_index, row in enumerate(matrix):
        if row:
            heappush(heap, (row[0], row_index, 0))

    result: list[int] = []
    while heap:
        value, row_index, col_index = heappop(heap)
        result.append(value)
        next_col = col_index + 1
        if next_col < len(matrix[row_index]):
            heappush(heap, (matrix[row_index][next_col], row_index, next_col))
    return result

