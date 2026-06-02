from conftest import load_kata


kata = load_kata("string_analysis")


def test_string_analysis():
    assert kata.char_frequencies("banana") == {"b": 1, "a": 3, "n": 2}
    assert kata.is_anagram("Debit card", "Bad credit")
    assert not kata.is_anagram("hello", "world")

