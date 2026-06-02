# Sorted Matrix Solution

The reference solution treats the rows as sorted streams and performs a k-way merge
with `heapq`.

The heap stores the next available value from each row. After popping one value, the
next value from the same row is pushed.

Complexity: `O(N log r)` time and `O(r)` space, where `r` is the number of rows.

