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

By default, tests run against the reference implementations in
`src/katastrof/solutions/`.

Each kata has its own folder:

```text
src/katastrof/katas/tail/
  __init__.py      # your implementation
  exercise.md      # clean exercise statement

src/katastrof/solutions/tail/
  __init__.py      # reference implementation
  explanation.md   # explanation of the solution
```

To practice, implement the matching `__init__.py` in `src/katastrof/katas/`, then
run the same contract tests against your code:

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_tail.py
```

Replace `tests/test_tail.py` with the test file for the kata you are solving.
Running the whole suite against `katastrof.katas` is useful only after you have
implemented every module.

## How to Train

1. Read one prompt in `docs/kata_catalog.md`.
2. Open the kata folder and read `exercise.md`.
3. Implement the matching `__init__.py` in `src/katastrof/katas/`.
4. Run the tests for fast feedback.
5. Compare with the matching solution folder, including `explanation.md`.
6. Read `docs/complexity_guide.md`.
7. Explain out loud the complexity and tradeoffs.

For sequencing, use `docs/study_plan.md`.

## Reset Progress

To reset all practice implementations back to stubs and clear the checkboxes in
`docs/study_plan.md`:

```bash
make reset-progress
```

This does not touch `src/katastrof/solutions/`.

## Reference Solution Style

The reference answers lean toward an Elixir-friendly Python style: small named
functions, comprehensions, generators, `Counter`, `all`, `reduce`, and recursive helpers
where they make the idea clearer. They still keep explicit loops for algorithms where
Python reads better that way, such as heap merging, graph traversal, thread
coordination, and early-exit searches.

## Elixir to Python Pointers

- Python lists are mutable; prefer returning new lists unless the exercise asks for
  in-place mutation.
- Python dictionaries and sets cover many Map/MapSet use cases.
- A Python `for` loop over an iterable often replaces recursive list traversal.
- Use generators for lazy streams, close to Elixir streams.
- Recursion exists, but Python has no tail-call optimization. Prefer iteration for
  deep traversals unless recursion is the point of the exercise.
