# Tail Solution

The reference solution turns the text into a generator of newline-free lines and feeds
that generator into a fixed-size `collections.deque`.

This mirrors a streaming implementation: even if the input is very large, memory usage
depends on the requested number of lines, not on the total input size.

Complexity: `O(n)` time and `O(count)` space.
