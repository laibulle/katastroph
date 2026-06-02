from conftest import load_kata


kata = load_kata("top_k_frequent")


def test_top_k_frequent():
    assert kata.top_k_frequent(["b", "a", "b", "c", "a", "b"], 2) == ["b", "a"]
    assert kata.top_k_frequent(["b", "a", "c"], 2) == ["a", "b"]
    assert kata.top_k_frequent([], 3) == []

