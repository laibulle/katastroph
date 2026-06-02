# Palindromes

Implement `make_palindromes(words: list[str]) -> list[str | None]`.

For each word, return one permutation that is a palindrome. If no palindrome can be
made, return `None` for that word.

Examples:

```python
make_palindromes(["aabb", "abc", "civic"]) == ["abba", None, "civic"]
```

A word can form a palindrome when at most one character appears an odd number of times.

