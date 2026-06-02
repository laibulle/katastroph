from operator import contains


def longest_distinct_substring(text: str) -> str:
    sub = ""
    current = ""
    for char in text:
        if len(current) > 0 and contains(current, char):
            if len(current) > len(sub):
                sub = current
            current = truncate_string(current, char)
        current += char

    return sub


def truncate_string(text: str, char: str) -> str:
    char_idx = 0
    for idx, str_char in enumerate(text):
        if char == str_char:
            char_idx = idx

    return text[char_idx:]







