import pytest

from conftest import load_kata


kata = load_kata("topological_sort")


def test_topological_sort_orders_dependencies_before_dependents():
    graph = {
        "shop": ["cook"],
        "cook": ["eat"],
        "clean": ["eat"],
        "eat": [],
    }
    order = kata.topological_sort(graph)
    positions = {node: index for index, node in enumerate(order)}
    assert positions["shop"] < positions["cook"] < positions["eat"]
    assert positions["clean"] < positions["eat"]


def test_topological_sort_rejects_cycles():
    with pytest.raises(ValueError):
        kata.topological_sort({"a": ["b"], "b": ["a"]})

