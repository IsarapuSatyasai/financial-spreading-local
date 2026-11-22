import pandas as pd
from pathlib import Path

def read_xlsx(path: str | Path) -> dict:
    """Read all sheets of an Excel file into a dict of DataFrames."""
    return pd.read_excel(path, sheet_name=None)
