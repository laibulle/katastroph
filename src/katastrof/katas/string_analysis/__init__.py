from functools import reduce


def char_frequencies(text: str) -> dict[str, int]:
    return reduce(lambda acc, item: acc | {item: acc.get(item, 0) + 1}, text, {})


def is_anagram(left: str, right: str) -> bool:
    raise NotImplementedError
