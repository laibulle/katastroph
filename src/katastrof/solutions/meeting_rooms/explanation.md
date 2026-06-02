# Meeting Rooms Solution

The solution separates starts and ends, sorts both, then sweeps through time.

Schema:

```text
starts: 0   5  15
ends:      10  20  30
rooms:  1   2   2
```

When a meeting starts before the earliest current end, a new room is needed. When the
start is after or equal to that end, one room is freed first.

Complexity: `O(n log n)` time for sorting and `O(n)` space for start/end lists.

