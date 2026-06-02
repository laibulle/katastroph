# Salut Toto

Implement `alternating_salut_toto(repetitions: int) -> str`.

Use two threads. One thread writes `"Salut"` and the other writes `"Toto"`. The output
must alternate deterministically.

Example:

```python
alternating_salut_toto(3) == "Salut Toto Salut Toto Salut Toto"
```

## Complexity Learning Goal

Let `n` be `repetitions`.

The output contains `2n` words, so the time and output space are both `O(n)`. The
interesting part is correctness of coordination, not asymptotic speed.

## Run the Test

```bash
KATA_PACKAGE=katastrof.katas uv run pytest tests/test_salut_toto.py
```

## LLM Review Prompt

Use this prompt after you have implemented the kata:

```text
You are reviewing my Python solution for the `salut_toto` kata.

Context:
- Exercise: `src/katastrof/katas/salut_toto/exercise.md`
- My solution: `src/katastrof/katas/salut_toto/__init__.py`
- Tests: `tests/test_salut_toto.py`
- Ideal reference solution written for this kata: `src/katastrof/solutions/salut_toto/__init__.py`
- Ideal explanation: `src/katastrof/solutions/salut_toto/explanation.md`

Please evaluate my solution on:
1. Correctness against the tests and edge cases.
2. Time and space complexity, using the variables from the exercise.
3. Python idiom and readability.
4. Whether my approach is reasonably close to the ideal solution, or if it is different but still valid.
5. The smallest concrete improvement I should make next.

Do not just paste the ideal solution. Explain the gap between my solution and the ideal solution.
```
