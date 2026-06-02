from collections import deque


def _reconstruct_path(parent: dict[str, str | None], goal: str) -> list[str]:
    path: list[str] = []
    node: str | None = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]


def shortest_path(graph: dict[str, list[str]], start: str, goal: str) -> list[str] | None:
    queue = deque([start])
    parent: dict[str, str | None] = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            return _reconstruct_path(parent, goal)
        for neighbor in graph.get(node, []):
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)

    return None

