# Tail

Implement `tail_lines(text: str, count: int) -> list[str]`.

Return the last `count` lines from `text`, like the Unix `tail` command. Lines in the
result should not include the trailing newline.

Examples:

```python
tail_lines("a\nb\nc\nd\n", 2) == ["c", "d"]
tail_lines("a\nb", 5) == ["a", "b"]
tail_lines("a\nb", 0) == []
```

Aim for `O(n)` time and `O(count)` space.

