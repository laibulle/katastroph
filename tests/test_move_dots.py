from conftest import load_kata


kata = load_kata("move_dots")


def test_move_dots_to_end():
    assert kata.move_dots_to_end(["a", "b", ".", "c", ".", ".", "k"]) == ["a", "b", "c", "k", ".", ".", "."]

