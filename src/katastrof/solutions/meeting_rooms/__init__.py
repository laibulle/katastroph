def min_meeting_rooms(meetings: list[tuple[int, int]]) -> int:
    starts = sorted(start for start, _ in meetings)
    ends = sorted(end for _, end in meetings)
    used = most_used = end_index = 0

    for start in starts:
        if start >= ends[end_index]:
            used -= 1
            end_index += 1
        used += 1
        most_used = max(most_used, used)

    return most_used

