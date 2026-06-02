# Sorted Matrix Solution

The reference solution treats the rows as sorted streams and performs a k-way merge
with `heapq`.

The initial heap is built with a list comprehension. A small helper pushes the next
value from the same row after each pop.

Complexity: `O(N log r)` time and `O(r)` space, where `r` is the number of rows.
