# Katastrof

Python algorithm kata for a first technical interview focused on general algorithms:
loops, trees, complexity, recursion, integers, prime numbers, string analysis, and data
structures.

The exercises are inspired by the SFEIR interview examples:
https://wiki.sfeir.com/carriere/recrutement/evaluation-algo/exemple_exercices_algo/

## Setup

```bash
uv sync --extra dev
uv run pytest
```

By default, tests run against the reference implementation in
`katastrof.solutions`.

To practice, implement the functions in `src/katastrof/katas.py`, then run the
same contract tests against your code:

```bash
KATA_MODULE=katastrof.katas uv run pytest
```

## How to Train

1. Read one prompt in `docs/kata_catalog.md`.
2. Implement the matching function in `src/katastrof/katas.py`.
3. Run the tests for fast feedback.
4. Compare with `src/katastrof/solutions.py`.
5. Explain out loud the complexity and tradeoffs.

## Elixir to Python Pointers

- Python lists are mutable; prefer returning new lists unless the exercise asks for
  in-place mutation.
- Python dictionaries and sets cover many Map/MapSet use cases.
- A Python `for` loop over an iterable often replaces recursive list traversal.
- Use generators for lazy streams, close to Elixir streams.
- Recursion exists, but Python has no tail-call optimization. Prefer iteration for
  deep traversals unless recursion is the point of the exercise.
