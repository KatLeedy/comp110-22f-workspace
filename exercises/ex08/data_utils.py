"""Dictionary related utility functions."""

__author__ = "730610012"


from csv import DictReader
from io import TextIOWrapper


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Reads each row from csv file into a list of str-str dictionaries."""
    row_table: list[dict[str, str]] = []
    file_handle: TextIOWrapper = open(filename, "r")
    csv_reader: DictReader[str] = DictReader(file_handle)
    for row in csv_reader:
        row_table.append(row)
    return row_table


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    """Returns all values of a certain column heading."""
    values: list[str] = []
    for row in table:
        values.append(row[column_name])
    return values


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms a row-oriented table of data into a dictionary of column headings and their values."""
    column_table: dict[str, list[str]] = {}
    for column_heading in row_table[0]:
        column_table[column_heading] = column_values(row_table, column_heading)
    return column_table


def head(full_column_table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Takes a full column-oriented data table and returns a smaller set with the first n rows of data for each column."""
    small_table: dict[str, list[str]] = {}
    n: int = num_rows
    if num_rows > len(full_column_table):
        n = len(full_column_table)
    for column_heading in full_column_table:
        some_values: list[str] = []
        i: int = 0
        while i < n:
            some_values.append(full_column_table[column_heading][i])
            i += 1
        small_table[column_heading] = some_values
    return small_table


def select(full_column_table: dict[str, list[str]], select_columns: list[str]) -> dict[str, list[str]]:
    """Given a list of desired column names, returns a table of only those columns and their values."""
    selected_data: dict[str, list[str]] = {}
    for column_name in select_columns:
        if column_name in full_column_table:
            selected_data[column_name] = full_column_table[column_name]
    return selected_data


def concat(column_table_1: dict[str, list[str]], column_table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two column-based tables into one column-based table."""
    combined_table: dict[str, list[str]] = {}
    for column in column_table_1:
        combined_table[column] = column_table_1[column]
    for column in column_table_2:
        if column in combined_table:
            combined_table[column] += column_table_2[column]
        else:
            combined_table[column] = column_table_2[column]
    return combined_table


def count(values: list[str]) -> dict[str, int]:
    """Counts up the unique values in a list of strings."""
    counts: dict[str, int] = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts