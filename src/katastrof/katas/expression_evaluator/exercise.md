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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `expression_evaluator` kata.

Context:
- Exercise: `src/katastrof/katas/expression_evaluator/exercise.md`
- My solution: `src/katastrof/katas/expression_evaluator/__init__.py`
- Tests: `tests/test_expression_evaluator.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/expression_evaluator/__init__.py`
- Ideal explanation: `src/katastrof/solutions/expression_evaluator/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
