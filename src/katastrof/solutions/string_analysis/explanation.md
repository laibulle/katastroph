# String Analysis Solution

The reference solution uses `collections.Counter`, Python's standard multiset.

For anagrams, a generator normalizes each string by lowercasing and removing spaces
before the counters are compared.

Complexity: `O(n + m)` time and `O(a)` space.
