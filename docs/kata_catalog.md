# Kata Catalog

Each kata has the same workflow: solve it in `src/katastrof/katas.py`, run the
tests, then compare with `src/katastrof/solutions.py`.

## SFEIR-Style Interview Exercises

### 1. Tail

Implement `tail_lines(text, count)`.

Return the last `count` lines of a text stream. The reference answer uses a fixed-size
`deque`, so memory is `O(count)` instead of `O(total_lines)`.

Complexity: `O(n)` time, `O(k)` space.

### 2. Serialization

Implement `serialize_graph(root)`.

Serialize a graph of object-like dictionaries, including cycles. Store each node once
and represent edges by ids.

Complexity: `O(V + E)` time, `O(V)` space.

### 3. Tableau de Palindromes

Implement `make_palindromes(words)`.

For each string, return one palindrome permutation or `None`. A palindrome permutation
is possible when at most one character has an odd count.

Complexity: `O(total_chars)` time, `O(alphabet)` space per word.

### 4. Caracteres Distincts

Implement `longest_distinct_substring(text)`.

Use a sliding window and a map of last-seen positions.

Complexity: `O(n)` time, `O(alphabet)` space.

### 5. En Commun

Implement `common_sorted(left, right)`.

Find common characters from two sorted lists, preserving duplicates. Use two pointers.

Complexity: `O(n + m)` time, `O(result)` space.

### 6. Salut Toto

Implement `alternating_salut_toto(repetitions)`.

Use two threads coordinated by a condition variable.

Complexity: `O(n)` time, `O(n)` output space.

### 7. Equilibrage

Implement `balanced_partition(numbers)`.

Split a list into two groups with minimum sum difference. This is the partition problem;
the exact reference answer uses dynamic programming over reachable sums.

Complexity: pseudo-polynomial `O(n * sum(numbers))` time and space.

### 8. Matrice Triee

Implement `merge_sorted_matrix(matrix)`.

Given a matrix where every row and column is sorted, return all elements in sorted
order. The reference answer performs a k-way merge of sorted rows using a heap.

Complexity: `O(N log rows)` time, `O(rows)` space.

### 9. Tassement

Implement `move_dots_to_end(items)`.

Move `"."` values to the end while preserving the relative order of other values.

Complexity: `O(n)` time, `O(n)` space.

## Core Algorithm Drills

### 10. Recursion

Implement `factorial_recursive(n)`.

Use recursion for the interview explanation, but remember that Python does not optimize
tail recursion.

### 11. Iteration

Implement `fibonacci_iterative(n)`.

This is the Pythonic version for production-sized inputs.

### 12. Integers

Implement `gcd(a, b)` with Euclid's algorithm.

Complexity: `O(log min(a, b))`.

### 13. Prime Numbers

Implement `is_prime(n)` and `primes_up_to(limit)`.

Use trial division up to `sqrt(n)` for primality and a sieve for many primes.

### 14. String Analysis

Implement `char_frequencies(text)` and `is_anagram(left, right)`.

Use `collections.Counter`, Python's standard multiset.

### 15. Stack

Implement `valid_parentheses(text)`.

Use a list as a stack.

### 16. Binary Search

Implement `binary_search(sorted_items, target)`.

The key invariant is that the answer, if present, remains inside `[low, high]`.

### 17. Trees

Implement `TreeNode`, `tree_height(node)`, `inorder_values(node)`, and
`breadth_first_values(root)`.

Depth-first traversal is naturally recursive; breadth-first traversal uses a queue.

### 18. Hash Set

Implement `two_sum(numbers, target)`.

Use a set of previously seen values to find a complement in one pass.

