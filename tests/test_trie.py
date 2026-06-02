from conftest import load_kata


kata = load_kata("trie")


def test_trie():
    trie = kata.Trie()
    trie.insert("cat")
    trie.insert("car")
    assert trie.contains("cat")
    assert trie.contains("car")
    assert not trie.contains("ca")
    assert trie.starts_with("ca")
    assert not trie.starts_with("dog")

