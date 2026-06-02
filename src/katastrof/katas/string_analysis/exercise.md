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
