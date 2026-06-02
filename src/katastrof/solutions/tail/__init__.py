from collections import deque
from io import StringIO


def _lines_without_newlines(text: str):
    return (line.removesuffix("\n") for line in StringIO(text))


def tail_lines(text: str, count: int) -> list[str]:
    """Return the last `count` lines of text."""
    if count <= 0:
        return []
    return list(deque(_lines_without_newlines(text), maxlen=count))
