import importlib
import os

import pytest


kata = importlib.import_module(os.getenv("KATA_MODULE", "katastrof.solutions"))


def test_tail_lines():
    assert kata.tail_lines("a\nb\nc\nd\n", 2) == ["c", "d"]
    assert kata.tail_lines("a\nb", 5) == ["a", "b"]
    assert kata.tail_lines("a\nb", 0) == []


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


def test_make_palindromes():
    assert kata.make_palindromes(["aabb", "abc", "civic"]) == ["abba", None, "civic"]


def test_longest_distinct_substring():
    assert kata.longest_distinct_substring("abcdemoderneancien") == "abcdemo"
    assert kata.longest_distinct_substring("abba") == "ab"
    assert kata.longest_distinct_substring("") == ""


def test_common_sorted():
    assert kata.common_sorted(["a", "e", "e", "e"], ["b", "b", "c", "e", "e", "g"]) == ["e", "e"]
    assert kata.common_sorted(["a", "b"], ["c", "d"]) == []


def test_alternating_salut_toto():
    assert kata.alternating_salut_toto(3) == "Salut Toto Salut Toto Salut Toto"
    assert kata.alternating_salut_toto(0) == ""


def test_balanced_partition():
    left, right = kata.balanced_partition([3, 1, 4, 2, 2])
    assert sorted(left + right) == [1, 2, 2, 3, 4]
    assert abs(sum(left) - sum(right)) == 0


def test_merge_sorted_matrix():
    matrix = [[1, 5, 9], [2, 6, 10], [3, 7, 11]]
    assert kata.merge_sorted_matrix(matrix) == [1, 2, 3, 5, 6, 7, 9, 10, 11]
    assert kata.merge_sorted_matrix([[], [1], []]) == [1]


def test_move_dots_to_end():
    assert kata.move_dots_to_end(["a", "b", ".", "c", ".", ".", "k"]) == ["a", "b", "c", "k", ".", ".", "."]


@pytest.mark.parametrize(
    ("n", "expected"),
    [(0, 1), (1, 1), (5, 120)],
)
def test_factorial_recursive(n, expected):
    assert kata.factorial_recursive(n) == expected


def test_fibonacci_iterative():
    assert [kata.fibonacci_iterative(n) for n in range(8)] == [0, 1, 1, 2, 3, 5, 8, 13]


def test_gcd():
    assert kata.gcd(54, 24) == 6
    assert kata.gcd(-54, 24) == 6
    assert kata.gcd(0, 5) == 5


def test_primes():
    assert kata.is_prime(2)
    assert kata.is_prime(97)
    assert not kata.is_prime(1)
    assert not kata.is_prime(100)
    assert kata.primes_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_string_analysis():
    assert kata.char_frequencies("banana") == {"b": 1, "a": 3, "n": 2}
    assert kata.is_anagram("Debit card", "Bad credit")
    assert not kata.is_anagram("hello", "world")


def test_valid_parentheses():
    assert kata.valid_parentheses("([]{})")
    assert kata.valid_parentheses("a(b[c]{d}e)")
    assert not kata.valid_parentheses("([)]")


def test_binary_search():
    assert kata.binary_search([1, 3, 5, 7], 5) == 2
    assert kata.binary_search([1, 3, 5, 7], 2) == -1


def test_tree_algorithms():
    root = kata.TreeNode(
        4,
        kata.TreeNode(2, kata.TreeNode(1), kata.TreeNode(3)),
        kata.TreeNode(6, kata.TreeNode(5), kata.TreeNode(7)),
    )
    assert kata.tree_height(root) == 3
    assert kata.inorder_values(root) == [1, 2, 3, 4, 5, 6, 7]
    assert kata.breadth_first_values(root) == [4, 2, 6, 1, 3, 5, 7]


def test_two_sum():
    assert kata.two_sum([10, 15, 3, 7], 17) == (10, 7)
    assert kata.two_sum([1, 2, 3], 99) is None

