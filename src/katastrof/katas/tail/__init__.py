LF = '\n'

def tail_lines(text: str, count: int) -> list[str]:
    current_count = count
    current_index = len(text) - 1
    latest_index = current_index
    lines = []

    if text[current_index] == LF:
        latest_index += 1

    while current_count > 0 and current_index > 0:
        if text[current_index] == LF:
            lines.insert(0, text[current_index-1:latest_index-1])
            latest_index = current_index - 1
            current_count -= 1

        current_index -= 1

    return lines