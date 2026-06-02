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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `graph_serialization` kata.

Context:
- Exercise: `src/katastrof/katas/graph_serialization/exercise.md`
- My solution: `src/katastrof/katas/graph_serialization/__init__.py`
- Tests: `tests/test_graph_serialization.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/graph_serialization/__init__.py`
- Ideal explanation: `src/katastrof/solutions/graph_serialization/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
