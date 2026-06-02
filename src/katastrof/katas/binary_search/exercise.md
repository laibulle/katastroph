# Binary Search

Implement `binary_search(sorted_items: list[int], target: int) -> int`.

Return the index of `target` in a sorted list, or `-1` when absent.

Examples:

```python
binary_search([1, 3, 5, 7], 5) == 2
binary_search([1, 3, 5, 7], 2) == -1
```

## Complexity Learning Goal

Let `n` be the list length.

Binary search is `O(log n)` because each comparison cuts the remaining search interval
roughly in half.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_binary_search.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `binary_search` kata.

Context:
- Exercise: `src/katastrof/katas/binary_search/exercise.md`
- My solution: `src/katastrof/katas/binary_search/__init__.py`
- Tests: `tests/test_binary_search.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/binary_search/__init__.py`
- Ideal explanation: `src/katastrof/solutions/binary_search/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
