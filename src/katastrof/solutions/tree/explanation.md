# Tree Traversal Solution

The reference solution represents nodes with a frozen dataclass.

Height and inorder traversal are natural recursive depth-first algorithms. The height
function maps itself over `(left, right)`, and inorder uses list unpacking to express
left-node-right order.

Breadth-first traversal uses a `collections.deque` as a queue and a helper that returns
the existing children for each node.

Complexity: each traversal is `O(n)` time. Recursive DFS uses `O(h)` call stack space;
BFS uses `O(w)` queue space.
