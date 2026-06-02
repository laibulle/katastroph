# String Analysis Solution

The reference solution uses `collections.Counter`, Python's standard multiset.

For anagrams, both strings are normalized by lowercasing and removing spaces before
comparing their counters.

Complexity: `O(n + m)` time and `O(a)` space.

