def valid_parentheses(text: str) -> bool:
    opened_pairs = []
    for c in text:
        is_opening = c in ["(", "[", "{", "<"]
        is_closing = c in [")", "]", "}", ">"]

        print(is_opening, is_closing)
        if is_opening:
            opened_pairs.append(c)
            print(opened_pairs)
        elif is_closing and is_matching_closing(opened_pairs[-1], c):
            opened_pairs.pop()
        elif is_closing:
            return False

    print(opened_pairs)
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
