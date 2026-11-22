"""Read CreditLens Excel template (local)."""
import pandas as pd
from src.graph.graph_state import FinancialGraphState
from src.template.excel_reader import read_xlsx

def read_template(state: FinancialGraphState) -> dict:
    excel_path = state["excel_path"]
    metrics = []
    try:
        dfs = read_xlsx(excel_path)
        for worksheet_name, df in dfs.items():
            for _, row in df.iterrows():
                variable = row.get("Variable")
                if variable and str(variable).strip() and variable not in ["table_name", "table_description"]:
                    metrics.append({
                        "worksheet": worksheet_name,
                        "variable": str(variable),
                        "description": str(row.get("Description", "")) if pd.notna(row.get("Description")) else None,
                        "formula": str(row.get("Formula", "")) if pd.notna(row.get("Formula")) else None,
                        "remarks": str(row.get("Remarks", "")) if pd.notna(row.get("Remarks")) else None,
                    })
        return {"excel_data": metrics, "errors": []}
    except Exception as e:
        return {"excel_data": [], "errors": [f"Excel read error: {str(e)}"]}
