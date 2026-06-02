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

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_tree.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `tree` kata.

Context:
- Exercise: `src/katastrof/katas/tree/exercise.md`
- My solution: `src/katastrof/katas/tree/__init__.py`
- Tests: `tests/test_tree.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/tree/__init__.py`
- Ideal explanation: `src/katastrof/solutions/tree/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
