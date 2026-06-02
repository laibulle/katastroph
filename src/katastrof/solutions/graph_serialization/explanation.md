# Graph Serialization Solution

The reference solution performs an iterative graph traversal with a stack and a `nodes`
dictionary keyed by id.

Small helpers name the important transformations: extracting ids, reading children, and
serializing one node. The dictionary is both the output store and the visited set. This
prevents infinite loops when cycles exist and ensures each node is serialized once.

Complexity: `O(V + E)` time and `O(V)` space.
