from conftest import load_kata


kata = load_kata("merge_intervals")


def test_merge_intervals():
    assert kata.merge_intervals([(1, 3), (2, 6), (8, 10), (9, 12)]) == [(1, 6), (8, 12)]
    assert kata.merge_intervals([(5, 7), (1, 2), (2, 4)]) == [(1, 4), (5, 7)]
    assert kata.merge_intervals([]) == []

