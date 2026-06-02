import pytest

from conftest import load_kata


kata = load_kata("max_sum_subarray")


def test_max_sum_subarray():
    assert kata.max_sum_subarray([2, 1, 5, 1, 3, 2], 3) == 9
    assert kata.max_sum_subarray([-2, -1, -5], 2) == -3


def test_max_sum_subarray_rejects_invalid_size():
    with pytest.raises(ValueError):
        kata.max_sum_subarray([1, 2], 0)

