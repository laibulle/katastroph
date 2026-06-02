# Two Sum Solution

The reference solution scans once and stores previously seen numbers in a set.

For each number, a helper either returns the matching pair or records the number in the
seen set. This keeps the public function focused on the search flow.

Complexity: `O(n)` average time and `O(n)` space.
