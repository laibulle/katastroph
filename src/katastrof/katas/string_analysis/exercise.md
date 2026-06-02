# String Analysis

Implement:

```python
char_frequencies(text: str) -> dict[str, int]
is_anagram(left: str, right: str) -> bool
```

`char_frequencies` counts characters. `is_anagram` should ignore spaces and casing.

Examples:

```python
char_frequencies("banana") == {"b": 1, "a": 3, "n": 2}
is_anagram("Debit card", "Bad credit") is True
```

## Complexity Learning Goal

Let `n` and `m` be the two string lengths.

Counting characters is linear: `O(n)` for one string, `O(n + m)` for comparing two
strings. The extra space depends on the number of distinct characters.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_string_analysis.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `string_analysis` kata.

Context:
- Exercise: `src/katastrof/katas/string_analysis/exercise.md`
- My solution: `src/katastrof/katas/string_analysis/__init__.py`
- Tests: `tests/test_string_analysis.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/string_analysis/__init__.py`
- Ideal explanation: `src/katastrof/solutions/string_analysis/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
