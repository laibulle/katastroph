# Balanced Partition Solution

The reference solution solves the exact partition problem with dynamic programming over
reachable sums.

It records which subtotal values can be built from the input, chooses the subtotal
closest to half of the total, then reconstructs one subset.

Complexity: pseudo-polynomial `O(n * sum(numbers))` time and space.

