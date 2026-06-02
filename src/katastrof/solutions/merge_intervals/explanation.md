# Merge Intervals Solution

The solution sorts intervals by start, then reduces them into a merged output list.

Schema:

```text
sorted:  [1,3] [2,6] [8,10] [9,12]
merge:   [1,6]       [8,12]
```

When the next interval starts after the previous merged interval ends, it begins a new
block. Otherwise, it extends the last merged block.

Complexity: `O(n log n)` time because of sorting, plus `O(n)` for the scan. Space is
`O(n)` for the result.

