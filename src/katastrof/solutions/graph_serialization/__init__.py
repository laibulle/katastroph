from typing import Any


def _node_id(node: dict[str, Any]) -> str:
    return str(node["id"])


def _children(node: dict[str, Any]) -> list[dict[str, Any]]:
    return node.get("children", [])


def _serialized_node(node: dict[str, Any]) -> dict[str, Any]:
    children = _children(node)
    return {
        "id": _node_id(node),
        "value": node.get("value"),
        "children": [_node_id(child) for child in children],
    }


def serialize_graph(root: dict[str, Any]) -> dict[str, Any]:
    """Serialize a graph of dict nodes that may contain cycles."""
    nodes: dict[str, dict[str, Any]] = {}
    stack = [root]
    while stack:
        node = stack.pop()
        node_id = _node_id(node)
        if node_id in nodes:
            continue
        nodes[node_id] = _serialized_node(node)
        stack.extend(_children(node))
    return {"root": _node_id(root), "nodes": nodes}
