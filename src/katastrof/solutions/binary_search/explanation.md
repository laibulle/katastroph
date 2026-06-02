# Binary Search Solution

The reference solution uses a small recursive helper that maintains an inclusive search
interval `[low, high]`.

At every step, it compares the middle value with the target and discards the half that
cannot contain the answer.

Complexity: `O(log n)` time and `O(log n)` call stack space. An iterative version would
keep the same time complexity and use `O(1)` space.
