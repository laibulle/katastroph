from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KATAS_DIR = ROOT / "src" / "katastrof" / "katas"
STUDY_PLAN = ROOT / "docs" / "study_plan.md"


TEMPLATES = {
    "balanced_partition": """def balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError
""",
    "binary_search": """def binary_search(sorted_items: list[int], target: int) -> int:
    raise NotImplementedError
""",
    "common_sorted": """def common_sorted(left: list[str], right: list[str]) -> list[str]:
    raise NotImplementedError
""",
    "expression_evaluator": """def evaluate(expression: str) -> int:
    raise NotImplementedError
""",
    "fibonacci": """def fibonacci_iterative(n: int) -> int:
    raise NotImplementedError
""",
    "gcd": """def gcd(a: int, b: int) -> int:
    raise NotImplementedError
""",
    "graph_serialization": """from typing import Any


def serialize_graph(root: dict[str, Any]) -> dict[str, Any]:
    raise NotImplementedError
""",
    "graph_shortest_path": """def shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    raise NotImplementedError
""",
    "longest_distinct_substring": """def longest_distinct_substring(text: str) -> str:
    raise NotImplementedError
""",
    "lru_cache": """class LRUCache:
    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key: str) -> int | None:
        raise NotImplementedError

    def put(self, key: str, value: int) -> None:
        raise NotImplementedError
""",
    "max_sum_subarray": """def max_sum_subarray(numbers: list[int], size: int) -> int:
    raise NotImplementedError
""",
    "meeting_rooms": """def min_meeting_rooms(meetings: list[tuple[int, int]]) -> int:
    raise NotImplementedError
""",
    "merge_intervals": """def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError
""",
    "move_dots": """def move_dots_to_end(items: list[str]) -> list[str]:
    raise NotImplementedError
""",
    "palindromes": """def make_palindromes(words: list[str]) -> list[str | None]:
    raise NotImplementedError
""",
    "parentheses": """def valid_parentheses(text: str) -> bool:
    raise NotImplementedError
""",
    "primes": """def is_prime(n: int) -> bool:
    raise NotImplementedError


def primes_up_to(limit: int) -> list[int]:
    raise NotImplementedError
""",
    "recursion": """def factorial_recursive(n: int) -> int:
    raise NotImplementedError
""",
    "salut_toto": """def alternating_salut_toto(repetitions: int) -> str:
    raise NotImplementedError
""",
    "sorted_matrix": """def merge_sorted_matrix(matrix: list[list[int]]) -> list[int]:
    raise NotImplementedError
""",
    "string_analysis": """def char_frequencies(text: str) -> dict[str, int]:
    raise NotImplementedError


def is_anagram(left: str, right: str) -> bool:
    raise NotImplementedError
""",
    "subsets": """def subsets(items: list[int]) -> list[list[int]]:
    raise NotImplementedError
""",
    "tail": """def tail_lines(text: str, count: int) -> list[str]:
    raise NotImplementedError
""",
    "top_k_frequent": """def top_k_frequent(items: list[str], k: int) -> list[str]:
    raise NotImplementedError
""",
    "topological_sort": """def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    raise NotImplementedError
""",
    "tree": """from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def tree_height(node: TreeNode | None) -> int:
    raise NotImplementedError


def inorder_values(node: TreeNode | None) -> list[int]:
    raise NotImplementedError


def breadth_first_values(root: TreeNode | None) -> list[int]:
    raise NotImplementedError
""",
    "trie": """class Trie:
    def insert(self, word: str) -> None:
        raise NotImplementedError

    def contains(self, word: str) -> bool:
        raise NotImplementedError

    def starts_with(self, prefix: str) -> bool:
        raise NotImplementedError
""",
    "two_sum": """from typing import Iterable


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError
""",
}


def reset_katas() -> None:
    for kata_name, template in sorted(TEMPLATES.items()):
        (KATAS_DIR / kata_name / "__init__.py").write_text(template, encoding="utf-8")


def reset_study_plan() -> None:
    text = STUDY_PLAN.read_text(encoding="utf-8")
    text = re.sub(r"- \[[xX]\]", "- [ ]", text)
    STUDY_PLAN.write_text(text, encoding="utf-8")


def main() -> None:
    reset_katas()
    reset_study_plan()
    print(f"Reset {len(TEMPLATES)} kata implementations and cleared study plan checkboxes.")


if __name__ == "__main__":
    main()
