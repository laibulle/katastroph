from collections import Counter


def make_palindromes(words: list[str]) -> list[str | None]:
    """Return one palindrome permutation for each word, or None if impossible."""
    return [_palindrome_permutation(word) for word in words]


def _palindrome_permutation(word: str) -> str | None:
    counts = Counter(word)
    odd = [char for char, n in counts.items() if n % 2 == 1]
    if len(odd) > 1:
        return None
    left = "".join(char * (counts[char] // 2) for char in sorted(counts))
    middle = odd[0] if odd else ""
    return left + middle + left[::-1]

