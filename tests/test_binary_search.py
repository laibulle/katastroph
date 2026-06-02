from conftest import load_kata


kata = load_kata("binary_search")


def test_binary_search():
    assert kata.binary_search([1, 3, 5, 7], 5) == 2
    assert kata.binary_search([1, 3, 5, 7], 2) == -1

