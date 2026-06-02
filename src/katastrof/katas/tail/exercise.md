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

## Complexity Learning Goal

Let `n` be the number of lines and `k` be `count`.

Aim for `O(n)` time because every line may need to be read once. Aim for `O(k)` space,
not `O(n)`, because keeping all lines is unnecessary.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_tail.py
```
