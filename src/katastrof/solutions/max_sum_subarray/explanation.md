# Max Sum Subarray Solution

The solution uses prefix sums. A window sum becomes one subtraction.

Schema:

```text
numbers:  2  1  5  1  3  2
prefix: 0 2  3  8  9 12 14

sum numbers[1:4] = prefix[4] - prefix[1] = 9 - 2 = 7
```

After prefix construction, every fixed-size window is evaluated in `O(1)`.

Complexity: `O(n)` time and `O(n)` space. A rolling-sum variant can reduce space to
`O(1)`.

