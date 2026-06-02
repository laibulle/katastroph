from collections import Counter


def make_palindromes(words: list[str]) -> list[str | None]:
    """Return one palindrome permutation for each word, or None if impossible."""
    return [_palindrome_permutation(word) for word in words]


def _palindrome_permutation(word: str) -> str | None:
    counts = Counter(word)
    odd = _odd_chars(counts)
    if len(odd) > 1:
        return None
    left = _left_half(counts)
    middle = _middle_char(odd)
    return left + middle + left[::-1]


def _odd_chars(counts: Counter[str]) -> list[str]:
    return [char for char, count in counts.items() if count % 2 == 1]


def _left_half(counts: Counter[str]) -> str:
    return "".join(char * (counts[char] // 2) for char in sorted(counts))


def _middle_char(odd_chars: list[str]) -> str:
    return odd_chars[0] if odd_chars else ""
