"""Unit tests for dictionary functions."""

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "123456789"


def test_invert_all_letters() -> None:
    """Tests invert function for a dictionary with single-letter keys and key-values."""
    a: dict[str, str] = {"a": "b", "c": "d", "e": "f"}
    assert invert(a) == {"b": "a", "d": "c", "f": "e"}


def test_invert_color_words() -> None:
    """Tests invert function for a dictionary with keys and key-values that are colors."""
    a: dict[str, str] = {"red": "blue", "yellow": "green", "orange": "purple"}
    assert invert(a) == {"blue": "red", "green": "yellow", "purple": "orange"}


def test_invert_empty_dict() -> None:
    """Tests invert function for an empty dictionary."""
    a: dict[str, str] = {}
    assert invert(a) == {}


def test_favorite_color_all_same_color() -> None:
    """Tests favorite_color on a dictionary where all values are the same."""
    dict1: dict[str, str] = {"person_1": "green", "person_2": "green", "person_3": "green"}
    assert favorite_color(dict1) == "green"


def test_favorite_color_yellow_most_common() -> None:
    """Tests favorite_color where yellow is the most common value."""
    dict1: dict[str, str] = {"person_1": "yellow", "person_2": "purple", "person_3": "yellow"}
    assert favorite_color(dict1) == "yellow"


def test_favorite_color_no_favorite() -> None:
    """Tests favorite_color when there is a tie."""
    dict1: dict[str, str] = {"person_1": "red", "person_2": "blue", "person_3": "red", "person_4": "blue"}
    assert favorite_color(dict1) == "red"


def test_count_every_item_different() -> None:
    """Tests count for a list where every item is different."""
    a: list[str] = ["high", "medium", "low"]
    assert count(a) == {"high": 1, "medium": 1, "low": 1}


def test_count_same_item_four_times() -> None:
    """Tests count for a list of the same item four times."""
    a: list[str] = ["happy", "happy", "happy", "happy"]
    assert count(a) == {"happy": 4}


def test_count_empty_list() -> None:
    """Tests count for an empty list."""
    a: list[str] = []
    assert count(a) == {}