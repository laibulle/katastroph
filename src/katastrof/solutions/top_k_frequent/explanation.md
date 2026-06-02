# Top K Frequent Solution

The solution counts values with `Counter`, then sorts unique values by two keys:
frequency descending and value ascending.

Schema:

```text
items:   b a b c a b
counts:  b=3, a=2, c=1
ranked:  b, a, c
```

Complexity: `O(n + u log u)` time and `O(u)` space, where `u` is the number of unique
values. A heap variant can be useful when `k` is much smaller than `u`.

