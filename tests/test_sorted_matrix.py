from conftest import load_kata


kata = load_kata("sorted_matrix")


def test_merge_sorted_matrix():
    matrix = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    assert kata.merge_sorted_matrix(matrix) == [1, 2, 3, 5, 6, 7, 9, 10, 11]
    assert kata.merge_sorted_matrix([[], [1], []]) == [1]

