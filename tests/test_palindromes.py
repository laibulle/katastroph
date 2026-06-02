from conftest import load_kata


kata = load_kata("palindromes")


def test_make_palindromes():
    assert kata.make_palindromes(["aabb", "abc", "civic"]) == ["abba", None, "civic"]

