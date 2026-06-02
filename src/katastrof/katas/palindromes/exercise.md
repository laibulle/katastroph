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
