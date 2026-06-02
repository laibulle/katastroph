# Expression Evaluator

Implement `evaluate(expression: str) -> int`.

Support non-negative integers, spaces, `+`, `-`, and parentheses.

Examples:

```python
evaluate("1 + 2 - 3") == 0
evaluate("1 + (2 - 3) + 4") == 4
```

## Complexity Learning Goal

Let `n` be the number of characters.

A single-pass parser should be `O(n)` time. Space is `O(d)` for parenthesis depth.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_expression_evaluator.py
```
