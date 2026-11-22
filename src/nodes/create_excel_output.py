"""Write results to Excel (local)."""
from src.graph.graph_state import FinancialGraphState
from src.template.excel_writer import write_results

def create_excel_output(state: FinancialGraphState) -> dict:
    answers = state.get("refined_answers") or state.get("answers", [])
    output_path = state.get("output_path")
    try:
        write_results(answers, output_path)
        return {"errors": state.get("errors", [])}
    except Exception as e:
        return {"errors": state.get("errors", []) + [f"Excel write error: {str(e)}"]}
