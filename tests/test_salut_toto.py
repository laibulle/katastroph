from conftest import load_kata


kata = load_kata("salut_toto")


def test_alternating_salut_toto():
    assert kata.alternating_salut_toto(3) == "Salut Toto Salut Toto Salut Toto"
    assert kata.alternating_salut_toto(0) == ""

