"""List utility functions part 2."""

__author__ = "730393320"


def only_evens(a: list[int]) -> list[int]:
    """Returns a list of only the even numbers in a list."""
    b: list[int] = []
    i: int = 0
    while i < len(a):
        if a[i] % 2 == 0:
            b.append(a[i])
        i += 1
    return b


def sub(a: list[int], b: int, c: int) -> list[int]:
    """Returns a list of the values between specified indices in another list."""
    new_list: list[int] = []
    if len(a) == 0 or b > len(a) or c - 1 <= 0:
        return []
    if b < 0:
        b = 0
    i: int = b  
    if c > len(a):
        c = len(a)
    while i < c:
        new_list.append(a[i])
        i += 1
    return new_list


def concat(a: list[int], b: list[int]) -> list[int]:
    """Returns a list comprised of the values of two lists."""
    new_list: list[int] = []
    i: int = 0
    while i < len(a):
        new_list.append(a[i])
        i += 1
    j: int = 0
    while j < len(b):
        new_list.append(b[j])
        j += 1
    return new_list