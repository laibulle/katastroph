from collections import Counter


def top_k_frequent(items: list[str], k: int) -> list[str]:
    counts = Counter(items)
    ranked = sorted(counts, key=lambda item: (-counts[item], item))
    return ranked[:k]

