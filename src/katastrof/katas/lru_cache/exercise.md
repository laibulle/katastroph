# LRU Cache

Implement an `LRUCache` with fixed capacity.

```python
cache = LRUCache(2)
cache.put("a", 1)
cache.put("b", 2)
cache.get("a") == 1
cache.put("c", 3)  # evicts "b"
```

## Complexity Learning Goal

Aim for `O(1)` average time for `get` and `put`.

In Python, `collections.OrderedDict` is the simplest idiomatic way to learn the idea.

