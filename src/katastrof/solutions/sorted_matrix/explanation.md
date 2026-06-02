# Sorted Matrix Solution

The reference solution treats the rows as sorted streams and performs a k-way merge
with `heapq`.

The initial heap is built with a list comprehension. A small helper pushes the next
value from the same row after each pop.

Schema:

```text
rows:
1  5  9
2  6 10
3  7 11

heap initially contains row heads: 1, 2, 3
pop 1, push 5
pop 2, push 6
```

Complexity: `O(N log r)` time and `O(r)` space, where `r` is the number of rows.
