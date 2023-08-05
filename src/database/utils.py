"""Utility functions"""
import sqlite3

def convert_rows_to_dicts(rows: list[sqlite3.Row]) -> list[dict]:
    """
    Convert sqlite3 list of rows to list of dictionaries (not in place)

    Parameters:
    rows (list[sqlite3.Row]): List of sqlite3 rows

    Returns:
    rows (list[dict]): list of rows as dictionaries
    """
    return list(
        map(dict, rows)
    )