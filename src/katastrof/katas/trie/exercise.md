# Trie

Implement a `Trie` with:

```python
insert(word)
contains(word)
starts_with(prefix)
```

A trie stores strings by shared prefixes.

## Complexity Learning Goal

Let `L` be the length of the word or prefix.

Insert, exact lookup, and prefix lookup should be `O(L)`, independent of how many words
are already stored.


## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_trie.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `trie` kata.

Context:
- Exercise: `src/katastrof/katas/trie/exercise.md`
- My solution: `src/katastrof/katas/trie/__init__.py`
- Tests: `tests/test_trie.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/trie/__init__.py`
- Ideal explanation: `src/katastrof/solutions/trie/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
