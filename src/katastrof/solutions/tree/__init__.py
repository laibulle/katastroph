from __future__ import annotations

from collections import deque
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeNode:
    value: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def _children(node: TreeNode) -> list[TreeNode]:
    return [child for child in (node.left, node.right) if child is not None]


def tree_height(node: TreeNode | None) -> int:
    return 0 if node is None else 1 + max(map(tree_height, (node.left, node.right)))


def inorder_values(node: TreeNode | None) -> list[int]:
    return [] if node is None else [
        *inorder_values(node.left),
        node.value,
        *inorder_values(node.right),
    ]


def breadth_first_values(root: TreeNode | None) -> list[int]:
    if root is None:
        return []
    queue: deque[TreeNode] = deque([root])
    values: list[int] = []
    while queue:
        node = queue.popleft()
        values.append(node.value)
        queue.extend(_children(node))
    return values
