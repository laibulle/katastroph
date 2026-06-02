def move_dots_to_end(items: list[str]) -> list[str]:
    """Move all '.' values to the end while preserving other item order."""
    compact = [item for item in items if item != "."]
    return compact + ["."] * (len(items) - len(compact))

