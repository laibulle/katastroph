from conftest import load_kata


kata = load_kata("graph_shortest_path")


def test_shortest_path():
    graph = {
        "a": ["b", "c"],
        "b": ["d"],
        "c": ["e"],
        "d": ["e"],
        "e": [],
    }
    assert kata.shortest_path(graph, "a", "e") == ["a", "c", "e"]
    assert kata.shortest_path(graph, "a", "missing") is None

