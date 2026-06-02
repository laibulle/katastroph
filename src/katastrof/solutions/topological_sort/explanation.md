# Topological Sort Solution

Kahn's algorithm repeatedly takes nodes with no remaining incoming edges.

Schema:

```text
shop -> cook -> eat
       clean -> eat

ready: [shop, clean]
```

When a node is emitted, its outgoing edges are removed conceptually by decrementing
incoming counts. If nodes remain but none are ready, there is a cycle.

Complexity: `O(V + E)` time and `O(V)` space.

