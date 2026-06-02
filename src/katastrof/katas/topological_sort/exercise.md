# Topological Sort

Implement `topological_sort(graph: dict[str, list[str]]) -> list[str]`.

The graph is directed. Return an ordering where every dependency appears before the
nodes that depend on it. Raise `ValueError` if the graph contains a cycle.

## Complexity Learning Goal

Let `V` be vertices and `E` be directed edges.

Kahn's algorithm is `O(V + E)` time and `O(V)` space.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_topological_sort.py
```
