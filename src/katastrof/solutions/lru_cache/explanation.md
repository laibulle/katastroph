# LRU Cache Solution

The cache combines hash lookup with recency ordering using `OrderedDict`.

Schema:

```text
least recent                     most recent
    b            a       get(a)       b            a
 [evict first]  [keep]   ---->    [evict first]  [moved]
```

Every successful `get` and every `put` moves the key to the most-recent end. If capacity
is exceeded, the least-recent item is popped from the front.

Complexity: `O(1)` average time for `get` and `put`, `O(capacity)` space.

