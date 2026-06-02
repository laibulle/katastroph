from typing import Any


def serialize_graph(root: dict[str, Any]) -> dict[str, Any]:
    """Serialize a graph of dict nodes that may contain cycles."""
    nodes: dict[str, dict[str, Any]] = {}
    stack = [root]
    while stack:
        node = stack.pop()
        node_id = str(node["id"])
        if node_id in nodes:
            continue
        children = node.get("children", [])
        nodes[node_id] = {
            "id": node_id,
            "value": node.get("value"),
            "children": [str(child["id"]) for child in children],
        }
        stack.extend(children)
    return {"root": str(root["id"]), "nodes": nodes}

