# Complexity Guide

Big-O describes how work grows when the input grows. It ignores exact machine speed and
small constants so you can compare algorithms by shape.

## The Core Vocabulary

`n` usually means "input size". Sometimes there are several sizes:

- `n`: length of one list or string
- `m`: length of another list or string
- `V`: number of graph vertices
- `E`: number of graph edges
- `h`: tree height
- `w`: maximum tree width
- `S`: sum of input numbers

## Common Shapes

```text
O(1)        constant       one lookup, one arithmetic operation
O(log n)    logarithmic    repeatedly cut the search space in half
O(n)        linear         visit every item once
O(n log n)  linearithmic   sorting, heap work over many items
O(n^2)      quadratic      compare every item with every other item
O(2^n)      exponential    try every subset or combination
```

## How To Estimate

1. Find the input size: list length, string length, tree nodes, graph edges.
2. Count how many times each item can be touched.
3. Drop constants: `2n` becomes `O(n)`.
4. Keep the dominant term: `n^2 + n` becomes `O(n^2)`.
5. Separate time from space.

## Elixir Mapping

The same reasoning applies to Elixir:

- `Enum.map(list, ...)` is `O(n)` because it visits every item.
- `Enum.reduce(list, acc, ...)` is `O(n)` for the same reason.
- `MapSet.member?(set, x)` is average `O(1)`.
- Recursing through a list once is `O(n)`.
- Nested `Enum.map` over the same list is often `O(n^2)`.

