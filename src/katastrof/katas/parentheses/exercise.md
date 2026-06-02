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
