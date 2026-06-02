# Trie Solution

A trie stores one character per edge, sharing common prefixes.

Schema:

```text
root
 └─ c
    └─ a
       ├─ t*
       └─ r*
```

`cat` and `car` share `c -> a`. `*` means "a complete word ends here".

Complexity: insert, contains, and starts-with are `O(L)` time, where `L` is the word or
prefix length. Space is proportional to the number of distinct prefix nodes stored.

