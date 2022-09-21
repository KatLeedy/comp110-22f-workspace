"""Tests for the utils functions."""

__author__ = "730610012"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests whether the only_evens function works on an empty list."""
    assert only_evens([]) == []


def test_only_evens_single_odd() -> None:
    """Tests whether the only_evens function works on a list with a single odd element."""
    assert only_evens([5]) == []


def test_only_evens_single_even() -> None:
    """Tests whether the only_evens function works on a list with a single even element."""
    assert only_evens([122]) == [122]


def test_only_evens_multiple() -> None:
    """Tests whether the only_evens function works on a list with several elements, both even and odd."""
    assert only_evens([3, 66, 2, 11, 9, 0, 324, 37]) == [66, 2, 0, 324]


def test_only_evens_with_negatives() -> None: 
    """Tests whether the only_evens function works on a list with several odd and even elements with some negative values."""
    assert only_evens([-1, 49, -16, 3, 5, 84]) == [-16, 84]


def test_concat_both_empty() -> None:
    """Tests whether the concat function works on two empty lists."""
    assert concat([], []) == []


def test_concat_one_empty() -> None:
    """Tests whether the concat function works on one empty list and one populated list."""
    assert concat([], [2, 5, -1]) == [2, 5, -1]


def test_concat_both_full() -> None:
    """Tests whether the concat function works on two populated lists."""
    assert concat([32, -19, 0, 0, 43], [12, 493, -9]) == [32, -19, 0, 0, 43, 12, 493, -9]


def test_sub_empty() -> None:
    """Tests whether the sub function works when passed an empty list."""
    assert sub([], 3, 6) == []


def test_sub_illogical_index() -> None:
    """Tests whether the sub function works when passed a start index higher than the length of the list."""
    assert sub([3, -1, 0, 43, 22, 51], 6, 5) == []


def test_sub_whole() -> None:
    """Tests whether the sub function returns a list with every number in the original list."""
    assert sub([4, 9, 10, -32], 0, 4) == [4, 9, 10, -32]


def test_sub_part() -> None: 
    """Tests whether the sub function returns a subset of a given list when the start and stop indexes given fit the expected bounds."""
    assert sub([23, -90, 5, 4, 111], 1, 4) == [-90, 5, 4]


def test_sub_part_2() -> None: 
    """Another test of whether the sub function returns a subset of a given list when the start and stop indexes given fit the expected bounds."""
    assert sub([4, 2, 0, -94342, 88, 123, -482], 0, 4) == [4, 2, 0, -94342]