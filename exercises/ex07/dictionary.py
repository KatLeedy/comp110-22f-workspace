"""Practice with basic dictionary functions."""

__author__ = "730610012"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of str-str key-value pairs, returns a dictionary with the keys and values reversed."""
    reverse_d: dict[str, str] = {}
    for item in d:  # loops through keys of d
        if d[item] in reverse_d:
            raise KeyError("Oops! There is a duplicate value that you are trying to make a key!")
        else:
            reverse_d[d[item]] = item
    return reverse_d


def favorite_color(d: dict[str, str]) -> str:
    """Given a dictionary of type [str, str], with the value being a color name, returns a str of the color that appears most frequently."""
    max_count: int = 0
    fav_color: str = ""
    for key in d:
        count: int = 0
        for k in d:
            if d[k] == d[key]:
                count += 1
        if count > max_count:
            max_count = count
            fav_color = d[key]
    return fav_color


def count(xs: list[str]) -> dict[str, int]:
    """Given a list of strings, produces a dictionary of str-int pairs where the value represents the count of how many times the key was encountered in the list."""
    counts_d: dict[str, int] = {}
    for item in xs:
        if item in counts_d:
            counts_d[item] += 1
        else:
            counts_d[item] = 1
    return counts_d