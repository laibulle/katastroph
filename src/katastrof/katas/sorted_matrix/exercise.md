# Sorted Matrix

Implement `merge_sorted_matrix(matrix: list[list[int]]) -> list[int]`.

Each row and each column are sorted in ascending order. Return all values in ascending
order.

Example:

```python
merge_sorted_matrix([[1, 5, 9], [2, 6, 10], [3, 7, 11]])
```

returns `[1, 2, 3, 5, 6, 7, 9, 10, 11]`.

## Complexity Learning Goal

Let `N` be the total number of values and `r` be the number of rows.

A heap-based merge should be `O(N log r)`: every value is popped once, and heap
operations cost `log r`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_sorted_matrix.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `sorted_matrix` kata.

Context:
- Exercise: `src/katastrof/katas/sorted_matrix/exercise.md`
- My solution: `src/katastrof/katas/sorted_matrix/__init__.py`
- Tests: `tests/test_sorted_matrix.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/sorted_matrix/__init__.py`
- Ideal explanation: `src/katastrof/solutions/sorted_matrix/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
