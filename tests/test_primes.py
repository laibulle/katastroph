from conftest import load_kata


kata = load_kata("primes")


def test_primes():
    assert kata.is_prime(2)
    assert kata.is_prime(97)
    assert not kata.is_prime(1)
    assert not kata.is_prime(100)
    assert kata.primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]

