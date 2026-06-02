# Study Plan

This plan assumes the first interview is general algorithms, not AI.

## Daily Session Shape

1. Pick one kata.
2. Read `exercise.md`.
3. Say the expected complexity out loud before coding.
4. Implement in `src/katastrof/katas/<kata>/__init__.py`.
5. Run the one matching test file.
6. Read `solutions/<kata>/explanation.md`.
7. Re-implement from memory once.

## Week 1: Python Algorithm Basics

- [x] `string_analysis`
- [x] `two_sum`
- [x] `parentheses`
- [x] `binary_search`
- [ ] `recursion`
- [ ] `fibonacci`
- [ ] `gcd`

Goal: become comfortable with Python collections, function signatures, tests, and simple
Big-O explanations.

## Week 2: Interview Patterns

- [ ] `longest_distinct_substring`
- [ ] `tail`
- [ ] `common_sorted`
- [ ] `move_dots`
- [ ] `tree`
- [ ] `primes`
- [ ] `merge_intervals`
- [ ] `meeting_rooms`

Goal: recognize linear scans, sorting-dominated solutions, stacks, queues, and sliding
windows.

## Week 3: Senior Patterns

- [ ] `graph_serialization`
- [ ] `graph_shortest_path`
- [ ] `topological_sort`
- [ ] `sorted_matrix`
- [ ] `lru_cache`
- [ ] `top_k_frequent`
- [ ] `expression_evaluator`

Goal: get comfortable with graphs, heaps, caches, parsing, and dependency ordering.

## Week 4: Harder Reasoning

- [ ] `balanced_partition`
- [ ] `subsets`
- [ ] revisit `longest_distinct_substring`
- [ ] revisit `topological_sort`
- [ ] revisit `expression_evaluator`

Goal: understand when complexity stops being linear: pseudo-polynomial dynamic
programming, exponential output size, and stack-based parsing.

## Interview Drill

For each solved kata, practice this explanation:

```text
I use <data structure> because <operation> must be fast.
The time complexity is <...> because <one sentence>.
The space complexity is <...> because <one sentence>.
One edge case is <...>.
```
