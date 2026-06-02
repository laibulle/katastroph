# Subsets Solution

For each item, duplicate all subsets seen so far: one copy without the item, one copy
with it.

Schema:

```text
start: [[]]
add 1: [[], [1]]
add 2: [[], [1], [2], [1,2]]
```

Complexity: `O(n * 2^n)` time if counting copied elements, and `O(n * 2^n)` output
space. The number of subsets alone is `2^n`.

