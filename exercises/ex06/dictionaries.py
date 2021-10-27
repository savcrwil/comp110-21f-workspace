"""Practice with dictionaries."""

__author__ = "730393320"


def invert(a: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and key-values of a dictionary."""
    b: dict[str, str] = {}
    for key in a:
        if a[key] in b:
            raise KeyError("Duplicate keys.")
        else:
            b[a[key]] = key
    return b


def favorite_color(dict1: dict[str, str]) -> str:
    """Returns the value that appears the most in a dictionary."""
    dict2: dict[str, int] = {}
    for key in dict1:
        if dict1[key] in dict2:
            dict2[dict1[key]] += 1
        else:
            dict2[dict1[key]] = 1
    max: int = 1
    for color in dict2:
        max = dict2[dict1[key]]
        max += 1
        # reassign max
        # max is a value of dict2
        # need to return the key associated with max


def count(a: list[str]) -> dict[str, int]:
    """Returns a dict of the number of times an item appears in a list."""
    b: dict[str, int] = {}
    for item in a:
        if item in b:
            b[item] += 1
        else:
            b[item] = 1
    return b
