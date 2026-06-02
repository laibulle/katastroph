def longest_distinct_substring(text: str) -> str:
    """Return the longest contiguous substring containing no repeated character."""
    start = 0
    best_start = 0
    best_len = 0
    last_seen: dict[str, int] = {}
    for index, char in enumerate(text):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = index
        window_len = index - start + 1
        if window_len > best_len:
            best_start = start
            best_len = window_len
    return text[best_start : best_start + best_len]

