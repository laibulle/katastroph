# Graph Shortest Path

Implement `shortest_path(graph, start, goal)`.

The graph is unweighted and represented as adjacency lists. Return the shortest path
from `start` to `goal`, or `None` when no path exists.

## Complexity Learning Goal

Let `V` be vertices and `E` be edges.

Breadth-first search is `O(V + E)` time because it visits each reachable vertex and edge
at most once. Space is `O(V)` for the queue and parent map.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_graph_shortest_path.py
```
