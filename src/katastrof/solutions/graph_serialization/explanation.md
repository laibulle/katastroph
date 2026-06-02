# Graph Serialization Solution

The reference solution performs an iterative graph traversal with a stack and a `nodes`
dictionary keyed by id.

The dictionary is both the output store and the visited set. This prevents infinite
loops when cycles exist and ensures each node is serialized once.

Complexity: `O(V + E)` time and `O(V)` space.

