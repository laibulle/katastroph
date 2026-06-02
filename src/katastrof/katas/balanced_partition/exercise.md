# Balanced Partition

Implement `balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]`.

Split the input into two groups such that the absolute difference between group sums is
as small as possible.

Example:

```python
left, right = balanced_partition([3, 1, 4, 2, 2])
abs(sum(left) - sum(right)) == 0
```

## Complexity Learning Goal

Let `n` be the number of values and `S` be their total sum.

An exact solution is usually pseudo-polynomial: `O(n * S)`. That means it depends on
the numeric values, not only on how many values there are.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_balanced_partition.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `balanced_partition` kata.

Context:
- Exercise: `src/katastrof/katas/balanced_partition/exercise.md`
- My solution: `src/katastrof/katas/balanced_partition/__init__.py`
- Tests: `tests/test_balanced_partition.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/balanced_partition/__init__.py`
- Ideal explanation: `src/katastrof/solutions/balanced_partition/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
