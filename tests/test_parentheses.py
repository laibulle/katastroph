from conftest import load_kata


kata = load_kata("parentheses")


def test_valid_parentheses():
    assert kata.valid_parentheses("([]{})")
    assert kata.valid_parentheses("a(b[c]{d}e)")
    assert not kata.valid_parentheses("([)]")

