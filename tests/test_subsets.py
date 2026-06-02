from conftest import load_kata


kata = load_kata("subsets")


def normalize(subsets):
    return sorted(tuple(sorted(subset)) for subset in subsets)


def test_subsets():
    assert normalize(kata.subsets([1, 2, 3])) == normalize(
        [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    )
    assert kata.subsets([]) == [[]]

