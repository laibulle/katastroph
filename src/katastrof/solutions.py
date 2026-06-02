"""Reference solutions for interview-style algorithm kata.

The implementations favor clarity, explicit invariants, and standard Python data
structures. That is usually what interviewers want before micro-optimizations.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from heapq import heappop, heappush
from io import StringIO
from math import isqrt
from threading import Condition, Thread
from typing import Any, Iterable


def tail_lines(text: str, count: int) -> list[str]:
    """Return the last `count` lines of text."""
    if count <= 0:
        return []
    last: deque[str] = deque(maxlen=count)
    for line in StringIO(text):
        last.append(line.removesuffix("\n"))
    return list(last)


def serialize_graph(root: dict[str, Any]) -> dict[str, Any]:
    """Serialize a graph of dict nodes that may contain cycles.

    Nodes are expected to have an `id` field and optional `children` list. The result
    stores each node once and represents edges by child ids.
    """
    nodes: dict[str, dict[str, Any]] = {}
    stack = [root]
    while stack:
        node = stack.pop()
        node_id = str(node["id"])
        if node_id in nodes:
            continue
        children = node.get("children", [])
        nodes[node_id] = {
            "id": node_id,
            "value": node.get("value"),
            "children": [str(child["id"]) for child in children],
        }
        stack.extend(children)
    return {"root": str(root["id"]), "nodes": nodes}


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


def common_sorted(left: list[str], right: list[str]) -> list[str]:
    """Return common items from two sorted lists, preserving duplicate counts."""
    i = j = 0
    result: list[str] = []
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            result.append(left[i])
            i += 1
            j += 1
        elif left[i] < right[j]:
            i += 1
        else:
            j += 1
    return result


def alternating_salut_toto(repetitions: int) -> str:
    """Use two threads to produce `Salut Toto` repeatedly in deterministic order."""
    if repetitions <= 0:
        return ""

    condition = Condition()
    turn = {"value": "salut"}
    output: list[str] = []

    def write(word: str, my_turn: str, next_turn: str) -> None:
        for _ in range(repetitions):
            with condition:
                condition.wait_for(lambda: turn["value"] == my_turn)
                output.append(word)
                turn["value"] = next_turn
                condition.notify_all()

    salut = Thread(target=write, args=("Salut", "salut", "toto"))
    toto = Thread(target=write, args=("Toto", "toto", "salut"))
    salut.start()
    toto.start()
    salut.join()
    toto.join()
    return " ".join(output)


def balanced_partition(numbers: list[int]) -> tuple[list[int], list[int]]:
    """Split numbers into two groups with the smallest possible sum difference."""
    total = sum(numbers)
    reachable: dict[int, int] = {0: -1}
    for index, value in enumerate(numbers):
        for subtotal in list(reachable):
            new_total = subtotal + value
            if new_total not in reachable:
                reachable[new_total] = index

    target = min(reachable, key=lambda subtotal: abs(total - 2 * subtotal))
    chosen_indices: set[int] = set()
    subtotal = target
    for index in range(len(numbers) - 1, -1, -1):
        value = numbers[index]
        if subtotal - value in reachable and reachable[subtotal] == index:
            chosen_indices.add(index)
            subtotal -= value

    left = [value for index, value in enumerate(numbers) if index in chosen_indices]
    right = [value for index, value in enumerate(numbers) if index not in chosen_indices]
    return left, right


def merge_sorted_matrix(matrix: list[list[int]]) -> list[int]:
    """Return all values from a row/column sorted matrix in ascending order."""
    heap: list[tuple[int, int, int]] = []
    for row_index, row in enumerate(matrix):
        if row:
            heappush(heap, (row[0], row_index, 0))

    result: list[int] = []
    while heap:
        value, row_index, col_index = heappop(heap)
        result.append(value)
        next_col = col_index + 1
        if next_col < len(matrix[row_index]):
            heappush(heap, (matrix[row_index][next_col], row_index, next_col))
    return result


def move_dots_to_end(items: list[str]) -> list[str]:
    """Move all '.' values to the end while preserving other item order."""
    compact = [item for item in items if item != "."]
    return compact + ["."] * (len(items) - len(compact))


def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is undefined for negative integers")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)


def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci is undefined for negative integers")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for divisor in range(3, isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False
    return True


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (((limit - start) // candidate) + 1)
    return [number for number, prime in enumerate(sieve) if prime]


def char_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(text))


def is_anagram(left: str, right: str) -> bool:
    normalize = lambda value: Counter(char.lower() for char in value if not char.isspace())
    return normalize(left) == normalize(right)


def valid_parentheses(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []
    for char in text:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def binary_search(sorted_items: list[int], target: int) -> int:
    low = 0
    high = len(sorted_items) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_items[middle] == target:
            return middle
        if sorted_items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1


@dataclass(frozen=True)
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def tree_height(node: TreeNode | None) -> int:
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def inorder_values(node: TreeNode | None) -> list[int]:
    if node is None:
        return []
    return inorder_values(node.left) + [node.value] + inorder_values(node.right)


def breadth_first_values(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    queue: deque[TreeNode] = deque([root])
    values: list[int] = []
    while queue:
        node = queue.popleft()
        values.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return values


def two_sum(numbers: Iterable[int], target: int) -> tuple[int, int] | None:
    seen: set[int] = set()
    for number in numbers:
        complement = target - number
        if complement in seen:
            return complement, number
        seen.add(number)
    return None

