from collections import Counter


def _normalized_chars(text: str):
    return (char.lower() for char in text if not char.isspace())


def char_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(text))


def is_anagram(left: str, right: str) -> bool:
    return Counter(_normalized_chars(left)) == Counter(_normalized_chars(right))
