# Tree Traversal

Implement:

```python
TreeNode
tree_height(node)
inorder_values(node)
breadth_first_values(root)
```

Use a binary tree. `inorder_values` should visit left subtree, node, then right subtree.
`breadth_first_values` should visit the tree level by level.

## Complexity Learning Goal

Let `n` be the number of nodes, `h` the tree height, and `w` the maximum width.

Traversals are `O(n)` time because every node is visited once. Recursive depth-first
search uses `O(h)` stack space. Breadth-first search uses `O(w)` queue space.
