# Tree Traversal Solution

The reference solution represents nodes with a frozen dataclass.

Height and inorder traversal are natural recursive depth-first algorithms. Breadth-first
traversal uses a `collections.deque` as a queue.

Complexity: each traversal is `O(n)` time. Recursive DFS uses `O(h)` call stack space;
BFS uses `O(w)` queue space.

