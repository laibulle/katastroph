# Graph Serialization

Implement `serialize_graph(root: dict[str, Any]) -> dict[str, Any]`.

The input is a graph of dictionaries. Each node has an `id`, may have a `value`, and may
have a `children` list. The graph may contain cycles.

Return a structure with:

- `root`: the root id
- `nodes`: one serialized record per discovered node

Edges should be represented by child ids, not by nested objects.

## Complexity Learning Goal

Let `V` be the number of nodes and `E` be the number of child links.

Aim for `O(V + E)` time: each node and edge should be handled once. Aim for `O(V)`
space for the serialized nodes and the visited set.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_graph_serialization.py
```
