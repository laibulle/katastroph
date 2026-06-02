from conftest import load_kata


kata = load_kata("two_sum")


def test_two_sum():
    assert kata.two_sum([10, 15, 3, 7], 17) == (10, 7)
    assert kata.two_sum([1, 2, 3], 99) is None

