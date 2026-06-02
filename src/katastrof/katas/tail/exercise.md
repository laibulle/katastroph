# Tail

Implement `tail_lines(text: str, count: int) -> list[str]`.

Return the last `count` lines from `text`, like the Unix `tail` command. Lines in the
result should not include the trailing newline.

Examples:

```python
tail_lines("a\nb\nc\nd\n", 2) == ["c", "d"]
tail_lines("a\nb", 5) == ["a", "b"]
tail_lines("a\nb", 0) == []
```

## Complexity Learning Goal

Let `n` be the number of lines and `k` be `count`.

Aim for `O(n)` time because every line may need to be read once. Aim for `O(k)` space,
not `O(n)`, because keeping all lines is unnecessary.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_tail.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `tail` kata.

Context:
- Exercise: `src/katastrof/katas/tail/exercise.md`
- My solution: `src/katastrof/katas/tail/__init__.py`
- Tests: `tests/test_tail.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/tail/__init__.py`
- Ideal explanation: `src/katastrof/solutions/tail/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
