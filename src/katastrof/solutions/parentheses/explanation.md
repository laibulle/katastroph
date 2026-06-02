# Parentheses Solution

The reference solution uses `functools.reduce` to apply one character transition at a
time to a stack.

Opening brackets are pushed onto the stack. Closing brackets must match the latest
opening bracket, or the reducer returns `None` to represent an invalid state. At the
end, the stack must be empty.

Schema:

```text
text:  ( [ ] )
stack: (      push
stack: ( [    push
stack: (      pop matching ]
stack: empty  pop matching )
```

Complexity: `O(n)` time and `O(n)` space.
