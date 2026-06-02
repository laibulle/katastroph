# Palindromes Solution

The reference solution counts characters with `collections.Counter`.

At most one character may have an odd count. Half of each character goes to the left
side, the optional odd character goes in the middle, and the mirrored left side becomes
the right side.

Complexity: `O(n + a log a)` per word, where `a` is the number of distinct characters.

