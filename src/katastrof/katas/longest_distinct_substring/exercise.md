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
