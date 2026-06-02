# Tail Solution

The reference solution turns the text into a generator of newline-free lines and feeds
that generator into a fixed-size `collections.deque`.

This mirrors a streaming implementation: even if the input is very large, memory usage
depends on the requested number of lines, not on the total input size.

Schema for `count = 3`:

```text
read a -> [a]
read b -> [a, b]
read c -> [a, b, c]
read d -> [b, c, d]
```

Complexity: `O(n)` time and `O(count)` space.
