# Parentheses

Implement `valid_parentheses(text: str) -> bool`.

Return whether every `()`, `[]`, and `{}` pair is correctly opened and closed. Other
characters should be ignored.

Examples:

```python
valid_parentheses("([]{})") is True
valid_parentheses("([)]") is False
```

## Complexity Learning Goal

Let `n` be the string length.

The stack solution is `O(n)` time because each character is read once. Space is `O(n)`
in the worst case, for example `"((((("`.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_parentheses.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `parentheses` kata.

Context:
- Exercise: `src/katastrof/katas/parentheses/exercise.md`
- My solution: `src/katastrof/katas/parentheses/__init__.py`
- Tests: `tests/test_parentheses.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/parentheses/__init__.py`
- Ideal explanation: `src/katastrof/solutions/parentheses/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
