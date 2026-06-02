# Balanced Partition Solution

The reference solution solves the exact partition problem with dynamic programming over
reachable sums.

`functools.reduce` applies one transition per input value to build the reachable subtotal
map. The map is updated in place during each transition so the dynamic-programming
complexity stays intact. Small helpers then choose the subtotal closest to half of the
total, reconstruct one subset, and split the original list by index.

Schema:

```text
numbers: 3, 1, 4
reachable sums:
start      {0}
after 3    {0, 3}
after 1    {0, 1, 3, 4}
after 4    {0, 1, 3, 4, 5, 7, 8}
```

Complexity: pseudo-polynomial `O(n * sum(numbers))` time and space.
