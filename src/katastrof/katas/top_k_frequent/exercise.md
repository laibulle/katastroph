# Top K Frequent

Implement `top_k_frequent(items: list[str], k: int) -> list[str]`.

Return the `k` most frequent values. Ties should be ordered alphabetically.

Example:

```python
top_k_frequent(["b", "a", "b", "c", "a", "b"], 2) == ["b", "a"]
```

## Complexity Learning Goal

Let `n` be the number of items and `u` the number of unique values.

Counting is `O(n)`. Sorting unique values is `O(u log u)`.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_top_k_frequent.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `top_k_frequent` kata.

Context:
- Exercise: `src/katastrof/katas/top_k_frequent/exercise.md`
- My solution: `src/katastrof/katas/top_k_frequent/__init__.py`
- Tests: `tests/test_top_k_frequent.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/top_k_frequent/__init__.py`
- Ideal explanation: `src/katastrof/solutions/top_k_frequent/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
