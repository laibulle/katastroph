# Longest Distinct Substring Solution

The reference solution uses a sliding window.

It stores the last seen index of each character. When a repeated character appears
inside the current window, the left boundary jumps after the previous occurrence.

Complexity: `O(n)` time and `O(a)` space, where `a` is the alphabet size.

