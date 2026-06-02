from __future__ import annotations

from collections import deque
from dataclasses import dataclass


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

