from conftest import load_kata


kata = load_kata("gcd")


def test_gcd():
    assert kata.gcd(54, 24) == 6
    assert kata.gcd(-54, 24) == 6
    assert kata.gcd(0, 5) == 5

