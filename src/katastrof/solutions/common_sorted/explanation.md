# Common Sorted Solution

The reference solution uses two pointers, one per sorted list.

When values match, it records the value and advances both pointers. Otherwise, it
advances the pointer with the smaller value.

Complexity: `O(n + m)` time and `O(result)` space.

