from conftest import load_kata


kata = load_kata("common_sorted")


def test_common_sorted():
    assert kata.common_sorted(["a", "e", "e", "e"], ["b", "b", "c", "e", "e", "g"]) == ["e", "e"]
    assert kata.common_sorted(["a", "b"], ["c", "d"]) == []

