from __future__ import annotations

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

