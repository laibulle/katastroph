import pytest

from conftest import load_kata


kata = load_kata("lru_cache")


def test_lru_cache_evicts_least_recently_used_key():
    cache = kata.LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") is None
    assert cache.get("a") == 1
    assert cache.get("c") == 3


def test_lru_cache_rejects_invalid_capacity():
    with pytest.raises(ValueError):
        kata.LRUCache(0)

