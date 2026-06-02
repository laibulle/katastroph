def valid_parentheses(text: str) -> bool:
    opened_pairs = []
    for c in text:
        is_opening = c in ["(", "[", "{", "<"]
        is_closing = c in [")", "]", "}", ">"]

        if is_opening:
            opened_pairs.append(c)
        elif is_closing and len(opened_pairs) == 0:
            return False
        elif is_closing and is_matching_closing(opened_pairs[-1], c):
            opened_pairs.pop()
        elif is_closing:
            return False

    return len(opened_pairs) == 0

def is_matching_closing(opening: str, closing: str) -> bool:
    match opening, closing:
        case ("(", ")"):
            return True
        case ("[", "]"):
            return True
        case ("{", "}"):
            return True
        case ("<", ">"):
            return True
        case _:
            return False
