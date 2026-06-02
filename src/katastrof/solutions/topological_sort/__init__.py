from collections import Counter, deque


def _all_nodes(graph: dict[str, list[str]]) -> set[str]:
    return set(graph) | {node for neighbors in graph.values() for node in neighbors}


def _incoming_counts(graph: dict[str, list[str]], nodes: set[str]) -> Counter[str]:
    counts: Counter[str] = Counter({node: 0 for node in nodes})
    counts.update(neighbor for neighbors in graph.values() for neighbor in neighbors)
    return counts


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    nodes = _all_nodes(graph)
    incoming = _incoming_counts(graph, nodes)
    ready = deque(node for node in nodes if incoming[node] == 0)
    order: list[str] = []

    while ready:
        node = ready.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            incoming[neighbor] -= 1
            if incoming[neighbor] == 0:
                ready.append(neighbor)

    if len(order) != len(nodes):
        raise ValueError("graph contains a cycle")
    return order

