# Common Sorted Solution

The reference solution uses `collections.Counter` as a multiset.

The `&` operator keeps the minimum count for each value that appears in both inputs.
`Counter.elements()` expands those counts back into values. Because the left input is
sorted, the resulting order is sorted too.

Complexity: `O(n + m + result)` time and `O(k)` space, where `k` is the number of
distinct common values.
