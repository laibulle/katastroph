from dataclasses import dataclass, replace
from functools import reduce


@dataclass(frozen=True)
class WindowState:
    start: int
    best_start: int
    best_len: int
    last_seen: dict[str, int]


def _slide_window(state: WindowState, indexed_char: tuple[int, str]) -> WindowState:
    index, char = indexed_char
    previous_index = state.last_seen.get(char, -1)
    start = max(state.start, previous_index + 1)
    window_len = index - start + 1
    best_start, best_len = (
        (start, window_len)
        if window_len > state.best_len
        else (state.best_start, state.best_len)
    )
    state.last_seen[char] = index
    return replace(
        state,
        start=start,
        best_start=best_start,
        best_len=best_len,
    )


def longest_distinct_substring(text: str) -> str:
    """Return the longest contiguous substring containing no repeated character."""
    state = reduce(_slide_window, enumerate(text), WindowState(0, 0, 0, {}))
    return text[state.best_start : state.best_start + state.best_len]
