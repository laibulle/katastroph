# Salut Toto Solution

The reference solution uses two `threading.Thread` instances coordinated by a
`threading.Condition`.

A shared `turn` value indicates which thread may write next. Each thread waits for its
turn, appends its word, flips the turn, and notifies the other thread.

Complexity: `O(n)` time and `O(n)` output space.

