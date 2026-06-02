from pathlib import Path


KATA_NAMES = {
    "balanced_partition",
    "binary_search",
    "common_sorted",
    "fibonacci",
    "gcd",
    "graph_serialization",
    "longest_distinct_substring",
    "move_dots",
    "palindromes",
    "parentheses",
    "primes",
    "recursion",
    "salut_toto",
    "sorted_matrix",
    "string_analysis",
    "tail",
    "tree",
    "two_sum",
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

