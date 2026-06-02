from conftest import load_kata


kata = load_kata("longest_distinct_substring")


def test_longest_distinct_substring():
    assert kata.longest_distinct_substring("abcdemoderneancien") == "abcdemo"
    assert kata.longest_distinct_substring("abba") == "ab"
    assert kata.longest_distinct_substring("") == ""

