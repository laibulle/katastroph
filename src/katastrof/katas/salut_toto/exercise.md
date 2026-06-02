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
