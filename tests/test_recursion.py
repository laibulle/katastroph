import pytest

from conftest import load_kata


kata = load_kata("recursion")


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 1), (1, 1), (5, 120)],
)
def test_factorial_recursive(n, expected):
    assert kata.factorial_recursive(n) == expected

