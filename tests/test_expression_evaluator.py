from conftest import load_kata


kata = load_kata("expression_evaluator")


def test_evaluate_expression():
    assert kata.evaluate("1 + 2 - 3") == 0
    assert kata.evaluate("1 + (2 - 3) + 4") == 4
    assert kata.evaluate("10 - (2 + 3) + 1") == 6
    assert kata.evaluate("42") == 42

