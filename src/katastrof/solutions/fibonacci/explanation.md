# Fibonacci Solution

The reference solution keeps only the previous two Fibonacci values and advances them
with `functools.reduce`.

This avoids the exponential recomputation of naive recursion and avoids recursion depth
limits.

Complexity: `O(n)` time and `O(1)` space.
