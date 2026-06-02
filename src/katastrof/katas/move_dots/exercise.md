# Move Dots

Implement `move_dots_to_end(items: list[str]) -> list[str]`.

Move every `"."` to the end of the list while preserving the relative order of every
other value.

Example:

```python
move_dots_to_end(["a", "b", ".", "c", ".", ".", "k"])
```

returns `["a", "b", "c", "k", ".", ".", "."]`.

## Complexity Learning Goal

Let `n` be the list length.

Aim for `O(n)` time: inspect each item once. Space can be `O(n)` for a clear solution,
or `O(1)` extra space for an in-place variant.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_move_dots.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `move_dots` kata.

Context:
- Exercise: `src/katastrof/katas/move_dots/exercise.md`
- My solution: `src/katastrof/katas/move_dots/__init__.py`
- Tests: `tests/test_move_dots.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/move_dots/__init__.py`
- Ideal explanation: `src/katastrof/solutions/move_dots/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
