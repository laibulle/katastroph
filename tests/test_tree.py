from conftest import load_kata


kata = load_kata("tree")


def test_tree_algorithms():
    root = kata.TreeNode(
        4,
        kata.TreeNode(2, kata.TreeNode(1), kata.TreeNode(3)),
        kata.TreeNode(6, kata.TreeNode(5), kata.TreeNode(7)),
    )
    assert kata.tree_height(root) == 3
    assert kata.inorder_values(root) == [1, 2, 3, 4, 5, 6, 7]
    assert kata.breadth_first_values(root) == [4, 2, 6, 1, 3, 5, 7]

