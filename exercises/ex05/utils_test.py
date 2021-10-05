"""Unit tests for list utility functions."""

from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730393320"

"""Tests for the only_evens function."""


def test_only_evens_empty_list() -> None:
    """Tests only_evens on an empty list."""
    a: list[int] = []
    assert only_evens(a) == []


def test_only_evens_3_item_list() -> None:
    """Tests only_evens on a list of 3 items."""
    a: list[int] = [47, 80, 32]
    assert only_evens(a) == [80, 32]


def test_only_evens_all_odds() -> None:
    """Tests only_evens on a list of odd numbers."""
    a: list[int] = [3, 5, 9, 1]
    assert only_evens(a) == []


"""Tests for the sub function."""


def test_sub_negative_start_index() -> None:
    """Tests sub when the start index is negative."""
    a: list[int] = [4, 6, 8, 7]
    b: int = -3
    c: int = 3
    assert sub(a, b, c) == [4, 6, 8]


def test_sub_start_param_greater_than_len() -> None:
    """Tests sub when the start index is greater than the length of the list."""
    a: list[int] = [1, 2, 3, 4, 5]
    b: int = 7
    c: int = 3
    assert sub(a, b, c) == []


def test_sub_normal_use_case() -> None:
    """Tests sub in a normal use case."""
    a: list[int] = [55, 66, 77, 88, 99]
    b: int = 1
    c: int = 4
    assert sub(a, b, c) == [66, 77, 88]


"""Tests for the concat function."""


def test_concat_empty_list() -> None:
    """Tests concat with two empty lists."""
    a: list[int] = []
    b: list[int] = []
    assert concat(a, b) == []


def test_concat_different_lens() -> None:
    """Tests concat with lists of different lengths."""
    a: list[int] = [7, 8, 9]
    b: list[int] = [1, 2]
    assert concat(a, b) == [7, 8, 9, 1, 2]


def test_concat_three_digit_nums() -> None:
    """Tests concat with lists comprised of three digit numbers."""
    a: list[int] = [679, 444]
    b: list[int] = [236, 784, 910]
    assert concat(a, b) == [679, 444, 236, 784, 910]
