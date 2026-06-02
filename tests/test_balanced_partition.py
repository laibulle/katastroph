from conftest import load_kata


kata = load_kata("balanced_partition")


def test_balanced_partition():
    left, right = kata.balanced_partition([3, 1, 4, 2, 2])
    assert sorted(left + right) == [1, 2, 2, 3, 4]
    assert abs(sum(left) - sum(right)) == 0

