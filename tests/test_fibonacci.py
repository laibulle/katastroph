from conftest import load_kata


kata = load_kata("fibonacci")


def test_fibonacci_iterative():
    assert [kata.fibonacci_iterative(n) for n in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]

