# Longest Distinct Substring

Implement `longest_distinct_substring(text: str) -> str`.

Return the longest contiguous substring containing no repeated character.

Examples:

```python
longest_distinct_substring("abcdemoderneancien") == "abcdemo"
longest_distinct_substring("abba") == "ab"
```

## Complexity Learning Goal

Let `n` be the string length.

Aim for `O(n)` time. A tempting solution checks every substring, which becomes `O(n^2)`
or worse. The intended solution moves a window across the string so each character is
processed once.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_longest_distinct_substring.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `longest_distinct_substring` kata.

Context:
- Exercise: `src/katastrof/katas/longest_distinct_substring/exercise.md`
- My solution: `src/katastrof/katas/longest_distinct_substring/__init__.py`
- Tests: `tests/test_longest_distinct_substring.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/longest_distinct_substring/__init__.py`
- Ideal explanation: `src/katastrof/solutions/longest_distinct_substring/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
