"""Utility functions."""

__author__ = "123456789"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # prepare to read the file as a csv rather than just strings
    csv_reader = DictReader(file_handle)
    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # close the file when done to free its resources
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(data: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Returns a dict with a certain number of key-value pairs."""
    new_dict: dict[str, list[str]] = {}

    for item in data:
        new_list: list[str] = []
        if number_rows > len(data[item]):
            number_rows = len(data[item])
        i: int = 0
        while i < number_rows:
            new_list.append(data[item][i])
            i += 1
        new_dict[item] = new_list
    return new_dict


def select(column_data: dict[str, list[str]], names_columns: list[str]) -> dict[str, list[str]]:
    """Returns a dict with a specific subset of the original columns."""
    new_dict: dict[str, list[str]] = {}
    for item in names_columns:
        new_dict[item] = column_data[item]
    return new_dict


def concat(a: dict[str, list[str]], b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines data from two different dicts into one."""
    c: dict[str, list[str]] = {}
    for item in a:
        c[item] = a[item]
    for item in b:
        c[item] = b[item]
    return c
    # this function doesn't work with duplicate values


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list."""
    b: dict[str, int] = {}
    for item in a:
        if item in b:
            b[item] += 1
        if item not in b:
            b[item] = 1
    
    return b


def filter(x: dict[str, list[str]], exclude: str, column: str) -> list[str]:
    """Filters out a specific key-value from a dictionary."""
    new_list: list[str] = []
   
    for item in x[column]:
        if item != exclude:
            new_list.append(item)
    return new_list
