from pathlib import Path


KATA_NAMES = {
    "balanced_partition",
    "binary_search",
    "common_sorted",
    "fibonacci",
    "gcd",
    "graph_serialization",
    "graph_shortest_path",
    "longest_distinct_substring",
    "lru_cache",
    "max_sum_subarray",
    "meeting_rooms",
    "merge_intervals",
    "move_dots",
    "palindromes",
    "parentheses",
    "primes",
    "recursion",
    "salut_toto",
    "sorted_matrix",
    "string_analysis",
    "subsets",
    "tail",
    "top_k_frequent",
    "topological_sort",
    "tree",
    "trie",
    "two_sum",
    "expression_evaluator",
}


def test_every_kata_has_a_folder_exercise_solution_and_explanation():
    root = Path(__file__).parents[1]

    for kata_name in KATA_NAMES:
        kata_dir = root / "src" / "katastrof" / "katas" / kata_name
        solution_dir = root / "src" / "katastrof" / "solutions" / kata_name

        assert (kata_dir / "__init__.py").exists()
        assert (kata_dir / "exercise.md").exists()
        assert (solution_dir / "__init__.py").exists()
        assert (solution_dir / "explanation.md").exists()


def test_curriculum_docs_exist():
    root = Path(__file__).parents[1]

    assert (root / "docs" / "kata_catalog.md").exists()
    assert (root / "docs" / "complexity_guide.md").exists()
    assert (root / "docs" / "study_plan.md").exists()
