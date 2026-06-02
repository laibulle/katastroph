# Meeting Rooms

Implement `min_meeting_rooms(meetings: list[tuple[int, int]]) -> int`.

Each meeting is `(start, end)`. Return the minimum number of rooms needed so no meetings
in the same room overlap.

Example:

```python
min_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
```

## Complexity Learning Goal

Let `n` be the number of meetings.

Sorting start and end times gives `O(n log n)` time. The sweep itself is `O(n)`.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_meeting_rooms.py
```
