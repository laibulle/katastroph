# Tail Solution

The reference solution scans the text once and stores only the latest `count` lines in
a fixed-size `collections.deque`.

This mirrors a streaming implementation: even if the input is very large, memory usage
depends on the requested number of lines, not on the total input size.

Complexity: `O(n)` time and `O(count)` space.

