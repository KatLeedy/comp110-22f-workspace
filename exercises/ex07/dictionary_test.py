"""Testing fuctions from the dictionary file."""

__author__ = "730610012"


from dictionary import invert, favorite_color, count
import pytest


def test_invert_empty() -> None:
    """Tests that the invert function returns empty dictionary when an empty dictionary is passed to it."""
    assert invert({}) == {}


def test_invert_one_item() -> None:
    """Tests whether the invert function switches the key and value of a dictionary with one item."""
    assert invert({"Hello": "Hi"}) == {"Hi": "Hello"}


def test_invert_many_items() -> None:
    """Tests the invert function when passed dictionary with many items."""
    assert invert({"Hello": "Hi", "Goodbye": "Bye", "Laughing": "Haha", "Yes": "y", "No": "N"})


def test_invert_KeyError() -> None:
    """Tests whether the invert function raises a KeyError when passed a dictionary with repeating values."""
    with pytest.raises(KeyError):
        my_dictionary = {"Laughing": "Hehe", "Chuckling": "Hehe"}
        invert(my_dictionary)


def test_favorite_color_empty() -> None:
    """Tests that the favorite_color function returns an empty string when an empty dictionary is passed to it."""
    assert favorite_color({}) == ""


def test_favorite_color_one_item() -> None:
    """Tests the favorite_color function when passed dictionary with only one item."""
    assert favorite_color({"Kat": "green"}) == "green"


def test_favorite_color_many_items() -> None:
    """Tests whether favorite_color function works on a dictionary of several key-value pairs."""
    assert favorite_color({"Kat": "green", "Ais": "blue", "Jeff": "green", "Misty": "blue", "Joe": "purple", "Helen": "blue"}) == "blue"


def test_favorite_color_tie() -> None:
    """Tests whether favorite_color function returns first value when two counts are tied in a dictionary."""
    assert favorite_color({"Kat": "green", "Ais": "blue", "Jeff": "green", "Misty": "blue", "Joe": "purple"}) == "green"


def test_count_empty() -> None:
    """Tests that count function called on empty list returns empty dict."""
    assert count([]) == {}


def test_count_one_item() -> None:
    """Tests whether count function works on a list with one item."""
    assert count(["single"]) == {"single": 1}


def test_count_many_items() -> None:
    """Tests whether count function works on a list with several items all of different number of occurences."""
    assert count(["a", "b", "c", "a", "a", "b", "d", "a", "c", "b"]) == {"a": 4, "b": 3, "c": 2, "d": 1}


def test_count_many_items_same_count() -> None:
    """Tests whether count function works on a list with several items that have similar number of occurences."""
    assert count(["a", "b", "c", "a", "b", "c"]) == {"a": 2, "b": 2, "c": 2}