# Subsets

Implement `subsets(items: list[int]) -> list[list[int]]`.

Return every subset of the input. Ordering of subsets is not important.

Example:

```python
subsets([1, 2]) == [[], [1], [2], [1, 2]]
```

## Complexity Learning Goal

Let `n` be the number of items.

There are `2^n` subsets, so any complete solution is at least `O(2^n)` time and space.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_subsets.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `subsets` kata.

Context:
- Exercise: `src/katastrof/katas/subsets/exercise.md`
- My solution: `src/katastrof/katas/subsets/__init__.py`
- Tests: `tests/test_subsets.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/subsets/__init__.py`
- Ideal explanation: `src/katastrof/solutions/subsets/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
