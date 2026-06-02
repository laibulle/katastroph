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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `meeting_rooms` kata.

Context:
- Exercise: `src/katastrof/katas/meeting_rooms/exercise.md`
- My solution: `src/katastrof/katas/meeting_rooms/__init__.py`
- Tests: `tests/test_meeting_rooms.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/meeting_rooms/__init__.py`
- Ideal explanation: `src/katastrof/solutions/meeting_rooms/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
