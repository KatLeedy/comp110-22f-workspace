"""An exercise in using lists to reproduce common functions."""

__author__ = "730610012"


def all(num_list: list[int], target: int) -> bool:
    """Takes a list of ints and returns a bool telling whether all the ints in the list are the same as a given int."""
    if len(num_list) == 0:
        return False
    i: int = 0
    while i < len(num_list):
        if num_list[i] != target:
            return False
        i += 1
    return True


def max(num_list2: list[int]) -> int:
    """Takes a list of ints and returns the largest one."""
    if len(num_list2) == 0:
        raise ValueError("max() arg is an empty List")
    j: int = 1
    current_max: int = num_list2[0]
    while j < len(num_list2):
        if num_list2[j] > current_max:
            current_max = num_list2[j]
        j += 1
    return current_max


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Takes two lists of ints and returns True if they are exactly the same."""
    if len(first_list) != len(second_list):
        return False
    k: int = 0
    while k < len(first_list):
        if first_list[k] != second_list[k]:
            return False
        k += 1
    return True