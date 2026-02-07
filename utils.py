import pandas as pd

def parse_date(series):
    return pd.to_datetime(series, errors="coerce")

def to_float(series):
    return pd.to_numeric(series, errors="coerce")