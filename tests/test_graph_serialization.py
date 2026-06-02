from conftest import load_kata


kata = load_kata("graph_serialization")


def test_serialize_graph_with_cycle():
    a = {"id": "a", "value": 1, "children": []}
    b = {"id": "b", "value": 2, "children": [a]}
    a["children"].append(b)
    assert kata.serialize_graph(a) == {
        "root": "a",
        "nodes": {
            "a": {"id": "a", "value": 1, "children": ["b"]},
            "b": {"id": "b", "value": 2, "children": ["a"]},
        },
    }

