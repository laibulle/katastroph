# Recursion Solution

The reference solution uses the mathematical recursive definition of factorial.

The base cases are `0` and `1`. Every larger input reduces the problem by calling
`factorial_recursive(n - 1)`.

Python does not optimize tail recursion, so this style is useful for explanation but
iteration is safer for very deep inputs.

