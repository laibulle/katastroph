from operator import contains


def longest_distinct_substring(text: str) -> str:
    sub = ""
    current = ""
    for char in text:
        if len(current) > 0 and contains(current, char):
            if len(current) > len(sub):
                sub = current
            current = ""
        current += char

    return sub







