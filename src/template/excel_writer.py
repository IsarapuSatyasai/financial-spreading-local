import pandas as pd
from pathlib import Path

def write_results(answers: list, output_path: str | Path):
    """Write extraction results to Excel."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(answers)
    if df.empty:
        df = pd.DataFrame([{"note": "No answers extracted"}])
    df.to_excel(output_path, index=False)
