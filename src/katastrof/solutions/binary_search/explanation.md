# Binary Search Solution

The reference solution maintains an inclusive search interval `[low, high]`.

At every step, it compares the middle value with the target and discards the half that
cannot contain the answer.

Complexity: `O(log n)` time and `O(1)` space.

