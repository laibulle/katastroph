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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `graph_shortest_path` kata.

Context:
- Exercise: `src/katastrof/katas/graph_shortest_path/exercise.md`
- My solution: `src/katastrof/katas/graph_shortest_path/__init__.py`
- Tests: `tests/test_graph_shortest_path.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/graph_shortest_path/__init__.py`
- Ideal explanation: `src/katastrof/solutions/graph_shortest_path/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
