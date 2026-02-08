import pandas as pd

"""
utils.py

Contains small helper functions used across the project.
These functions isolate repetitive tasks such as type
conversion and validation.

Keeping helpers here improves reusability and readability.
"""

def parse_date(series):
    """
    Safely convert a pandas Series to datetime.
    Invalid values are converted to NaT.
    """
    return pd.to_datetime(series, errors="coerce")

def to_float(series):
    """
    Safely convert a pandas Series to numeric values.
    Invalid values are converted to NaN.
    """
    return pd.to_numeric(series, errors="coerce")