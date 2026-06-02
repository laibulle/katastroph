# Common Sorted

Implement `common_sorted(left: list[str], right: list[str]) -> list[str]`.

Both input lists are sorted. Return the common values while preserving duplicate counts.

Example:

```python
common_sorted(["a", "e", "e", "e"], ["b", "b", "c", "e", "e", "g"]) == ["e", "e"]
```

## Complexity Learning Goal

Let `n` and `m` be the input lengths.

Aim for work proportional to both inputs: `O(n + m)`. Avoid checking every item from
the first list against every item from the second list, which would be `O(n * m)`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_common_sorted.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `common_sorted` kata.

Context:
- Exercise: `src/katastrof/katas/common_sorted/exercise.md`
- My solution: `src/katastrof/katas/common_sorted/__init__.py`
- Tests: `tests/test_common_sorted.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/common_sorted/__init__.py`
- Ideal explanation: `src/katastrof/solutions/common_sorted/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
