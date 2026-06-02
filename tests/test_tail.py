from conftest import load_kata


kata = load_kata("tail")


def test_tail_lines():
    assert kata.tail_lines("a\nb\nc\nd\n", 2) == ["c", "d"]
    assert kata.tail_lines("a\nb", 5) == ["a", "b"]
    assert kata.tail_lines("a\nb", 0) == []

