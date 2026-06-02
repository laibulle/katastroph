# Palindromes

Implement `make_palindromes(words: list[str]) -> list[str | None]`.

For each word, return one permutation that is a palindrome. If no palindrome can be
made, return `None` for that word.

Examples:

```python
make_palindromes(["aabb", "abc", "civic"]) == ["abba", None, "civic"]
```

A word can form a palindrome when at most one character appears an odd number of times.

## Complexity Learning Goal

Let `n` be the total number of characters.

Counting characters is `O(n)`. Building the answer is also linear in the characters you
output. The important interview point is that you do not try every permutation.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_palindromes.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `palindromes` kata.

Context:
- Exercise: `src/katastrof/katas/palindromes/exercise.md`
- My solution: `src/katastrof/katas/palindromes/__init__.py`
- Tests: `tests/test_palindromes.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/palindromes/__init__.py`
- Ideal explanation: `src/katastrof/solutions/palindromes/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
