# Graph Serialization

Implement `serialize_graph(root: dict[str, Any]) -> dict[str, Any]`.

The input is a graph of dictionaries. Each node has an `id`, may have a `value`, and may
have a `children` list. The graph may contain cycles.

Return a structure with:

- `root`: the root id
- `nodes`: one serialized record per discovered node

Edges should be represented by child ids, not by nested objects.

Aim for `O(V + E)` time and `O(V)` space.

