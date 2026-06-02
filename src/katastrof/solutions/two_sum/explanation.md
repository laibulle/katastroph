# Two Sum Solution

The reference solution scans once and stores previously seen numbers in a set.

For each number, it checks whether `target - number` has already been seen. If so, the
pair is found immediately.

Complexity: `O(n)` average time and `O(n)` space.

