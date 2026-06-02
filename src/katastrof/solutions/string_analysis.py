from collections import Counter


def char_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(text))


def is_anagram(left: str, right: str) -> bool:
    normalize = lambda value: Counter(char.lower() for char in value if not char.isspace())
    return normalize(left) == normalize(right)

