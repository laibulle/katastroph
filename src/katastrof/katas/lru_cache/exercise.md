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


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_lru_cache.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `lru_cache` kata.

Context:
- Exercise: `src/katastrof/katas/lru_cache/exercise.md`
- My solution: `src/katastrof/katas/lru_cache/__init__.py`
- Tests: `tests/test_lru_cache.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/lru_cache/__init__.py`
- Ideal explanation: `src/katastrof/solutions/lru_cache/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
