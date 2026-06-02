# Greatest Common Divisor Solution

The reference solution uses Euclid's algorithm: repeatedly replace `(a, b)` with
`(b, a % b)` until `b` is zero.

Absolute values normalize negative inputs.

Complexity: `O(log min(a, b))`.

