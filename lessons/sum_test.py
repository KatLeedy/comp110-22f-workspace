"""Tests for the sum function."""


from lessons.sum import sum


def test_sum_empty() -> None:
    assert sum([]) == 0.0


def test_sum_single_item() -> None: 
   # just showing that you can define a variable in the function here
    xs: list[float] = [110.0]
    assert sum(xs) == 110.0


def test_sum_many_items() -> None:
    assert sum([1.0, 2.0, 3.0]) == 6.0