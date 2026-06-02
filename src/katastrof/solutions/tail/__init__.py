from collections import deque
from io import StringIO


def tail_lines(text: str, count: int) -> list[str]:
    """Return the last `count` lines of text."""
    if count <= 0:
        return []
    last: deque[str] = deque(maxlen=count)
    for line in StringIO(text):
        last.append(line.removesuffix("\n"))
    return list(last)

