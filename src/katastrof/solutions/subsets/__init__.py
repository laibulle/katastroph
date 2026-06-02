from functools import reduce


def _add_item(existing: list[list[int]], item: int) -> list[list[int]]:
    return [*existing, *[subset + [item] for subset in existing]]


def subsets(items: list[int]) -> list[list[int]]:
    return reduce(_add_item, items, [[]])

