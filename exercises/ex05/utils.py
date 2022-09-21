"""An exercise in creating list-traversing functions to use to practice unit testing."""

__author__ = "730610012"


def only_evens(xs: list[int]) -> list[int]:
    """Given a list of ints, returns a list containing only the even values."""
    even_list: list[int] = []
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 == 0:
            even_list.append(xs[i])
        i += 1
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists of ints, returns a list with all the elements of the first list followed by all elements of the second list."""
    combined_list: list[int] = []
    i: int = 0
    while i < len(list_one): 
        combined_list.append(list_one[i])
        i += 1
    j: int = 0
    while j < len(list_two): 
        combined_list.append(list_two[j])
        j += 1
    return combined_list


def sub(long_list: list[int], start_index: int, stop_index: int) -> list[int]:
    """Given a list of ints and two integer index values, returns a list of the list elements between the first index and the second index - 1."""
    # Returns empty list if the original list is empty, or if the start/stop index values are completely outside the bounds
    if len(long_list) == 0 or start_index > len(long_list) or stop_index <= 0:
        return []
        # Need to check if it should be start_index >= len(long_list)
    short_list: list[int] = []
    st: int = 0
    end: int = len(long_list)
    # Sets the index values to the given start and stop values if they are within the length of the list
    if start_index > 0:
        st = start_index
    if stop_index < len(long_list):
        end = stop_index
    while st < end:
        short_list.append(long_list[st])
        st += 1
    return short_list