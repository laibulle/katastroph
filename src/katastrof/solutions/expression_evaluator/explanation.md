# Expression Evaluator Solution

The parser keeps a running `total`, current `sign`, and current `number`.

Schema:

```text
1 + (2 - 3) + 4
    push total/sign at "("
        evaluate inner: -1
    pop and combine
```

Parentheses save the outer context on a stack. When `)` appears, the inner total is
combined with the previous total and sign.

Complexity: `O(n)` time and `O(d)` space, where `d` is parenthesis depth.

