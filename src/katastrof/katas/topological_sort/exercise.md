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

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `topological_sort` kata.

Context:
- Exercise: `src/katastrof/katas/topological_sort/exercise.md`
- My solution: `src/katastrof/katas/topological_sort/__init__.py`
- Tests: `tests/test_topological_sort.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/topological_sort/__init__.py`
- Ideal explanation: `src/katastrof/solutions/topological_sort/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
