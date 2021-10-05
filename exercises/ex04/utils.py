"""List utility functions."""

__author__ = "730393320"


def all(a: list[int], b: int) -> bool:
    """Determines if all values in a list are equal to a number."""
    if len(a) == 0:
        return False
    i: int = 0
    while i < len(a):
        if a[i] != b:
            return False
        i += 1
    return True


def is_equal(c: list[int], d: list[int]) -> bool:
    """Determines deep equality of two lists of ints."""
    if len(c) == 0 and len(d) == 0:
        return True
    if len(c) != len(d):
        return False
    i: int = 0
    while i < len(c):
        if c[i] != d[i]:
            return False
        i += 1
    return True


def max(e: list[int]) -> int:
    """Returns the largest value in a list of ints."""
    if len(e) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max: int = e[0]
    while i < len(e):
        if e[i] > max:
            max = e[i]
        i += 1
    return max
    