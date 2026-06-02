# Longest Distinct Substring Solution

The reference solution uses a sliding window represented by a small `WindowState`
dataclass.

`functools.reduce` applies one transition per indexed character. The state stores the
current window start, the best window found so far, and the last seen index for each
character. The dictionary is updated in place so the algorithm keeps linear time.

Schema:

```text
text:  a b b a
       [a b]       best = "ab"
         [b]       second b moves start
         [b a]     best still "ab"
```

Complexity: `O(n)` time and `O(a)` space, where `a` is the alphabet size.
