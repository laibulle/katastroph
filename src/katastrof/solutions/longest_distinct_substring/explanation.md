# Longest Distinct Substring Solution

The reference solution uses a sliding window represented by a small `WindowState`
dataclass.

`functools.reduce` applies one transition per indexed character. The state stores the
current window start, the best window found so far, and the last seen index for each
character. The dictionary is updated in place so the algorithm keeps linear time.

Complexity: `O(n)` time and `O(a)` space, where `a` is the alphabet size.
