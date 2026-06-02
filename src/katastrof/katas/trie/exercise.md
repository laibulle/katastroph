# Trie

Implement a `Trie` with:

```python
insert(word)
contains(word)
starts_with(prefix)
```

A trie stores strings by shared prefixes.

## Complexity Learning Goal

Let `L` be the length of the word or prefix.

Insert, exact lookup, and prefix lookup should be `O(L)`, independent of how many words
are already stored.

