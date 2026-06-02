# Balanced Partition Solution

The reference solution solves the exact partition problem with dynamic programming over
reachable sums.

`functools.reduce` applies one transition per input value to build the reachable subtotal
map. The map is updated in place during each transition so the dynamic-programming
complexity stays intact. Small helpers then choose the subtotal closest to half of the
total, reconstruct one subset, and split the original list by index.

Complexity: pseudo-polynomial `O(n * sum(numbers))` time and space.
