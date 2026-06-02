# Kata Catalog

Each kata has the same workflow: read `exercise.md` in the matching folder under
`src/katastrof/katas/`, implement `__init__.py`, run the test, then compare with the
matching folder under `src/katastrof/solutions/`.

This curriculum stays non-AI for now. It targets the general algorithm interview skills
you need before an AI-integration role gets into product architecture, LLM workflows, or
model APIs.

## Track 1: Core Python Algorithms

These kata build the foundations: Python syntax, standard collections, recursion,
strings, integers, and basic data structures.

| Kata | Pattern | Target Complexity |
| --- | --- | --- |
| `tail` | streaming, deque | `O(n)` time, `O(k)` space |
| `palindromes` | counting, `Counter` | `O(n)` time |
| `longest_distinct_substring` | sliding window | `O(n)` time |
| `common_sorted` | multiset / two lists | `O(n + m)` time |
| `move_dots` | stable compaction | `O(n)` time |
| `recursion` | recursive base case | `O(n)` time |
| `fibonacci` | iterative/reduce state | `O(n)` time, `O(1)` space |
| `gcd` | Euclid recursion | `O(log min(a, b))` |
| `primes` | divisibility, sieve | `O(sqrt(n))`, sieve about `O(n log log n)` |
| `string_analysis` | normalization, `Counter` | `O(n + m)` time |
| `parentheses` | stack | `O(n)` time |
| `binary_search` | halve search space | `O(log n)` time |
| `tree` | DFS/BFS | `O(n)` time |
| `two_sum` | hash set lookup | `O(n)` average time |

## Track 2: SFEIR-Style Exercises

These map closely to the exercises from the interview guidance you shared.

| Kata | Pattern | Target Complexity |
| --- | --- | --- |
| `graph_serialization` | graph traversal with cycles | `O(V + E)` |
| `salut_toto` | thread coordination | `O(n)` output |
| `balanced_partition` | dynamic programming | `O(n * S)` pseudo-polynomial |
| `sorted_matrix` | heap / k-way merge | `O(N log r)` |

## Track 3: Senior Interview Patterns

These are the next layer for senior readiness. They are still general algorithms, but
they show up constantly in integration-heavy systems: schedulers, queues, caches,
dependency graphs, parsers, and ranking.

| Kata | Pattern | Target Complexity |
| --- | --- | --- |
| `merge_intervals` | intervals + sorting | `O(n log n)` |
| `meeting_rooms` | sweep line | `O(n log n)` |
| `graph_shortest_path` | BFS shortest path | `O(V + E)` |
| `topological_sort` | dependency ordering | `O(V + E)` |
| `trie` | prefix tree | `O(L)` per operation |
| `lru_cache` | cache eviction | `O(1)` average operations |
| `max_sum_subarray` | fixed sliding window / prefix sums | `O(n)` |
| `subsets` | backtracking / powerset | `O(n * 2^n)` output |
| `expression_evaluator` | parsing + stack | `O(n)` |
| `top_k_frequent` | counting + ranking | `O(n + u log u)` |

## Suggested Order

1. Start with `string_analysis`, `two_sum`, `parentheses`, `binary_search`.
2. Move to `longest_distinct_substring`, `tail`, `tree`, `primes`.
3. Do SFEIR-style kata: `graph_serialization`, `sorted_matrix`, `balanced_partition`.
4. Finish with senior patterns: `merge_intervals`, `meeting_rooms`,
   `graph_shortest_path`, `topological_sort`, `lru_cache`, `expression_evaluator`.

For every kata, force yourself to answer three questions before reading the solution:

- What is `n`?
- How many times can one input item be touched?
- What extra data structure grows with the input?

