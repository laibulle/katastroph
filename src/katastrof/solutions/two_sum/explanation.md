# Two Sum Solution

The reference solution scans once and stores previously seen numbers in a set.

For each number, a helper either returns the matching pair or records the number in the
seen set. This keeps the public function focused on the search flow.

Schema:

```text
target = 17

10 -> need 7   seen={}
15 -> need 2   seen={10}
3  -> need 14  seen={10,15}
7  -> need 10  seen={10,15,3}  found
```

Complexity: `O(n)` average time and `O(n)` space.
