# Graph Shortest Path Solution

Breadth-first search explores by distance: all nodes at distance 1, then distance 2,
and so on. The first time the goal is reached, the path is shortest.

Schema:

```text
A
| \
B  C
|  |
D--E

queue levels from A: [A] -> [B, C] -> [D, E]
```

The `parent` map remembers how each node was reached, then the path is reconstructed
backward from the goal.

Complexity: `O(V + E)` time and `O(V)` space.

