"""Simple pass-through refinement (local)."""
from src.graph.graph_state import FinancialGraphState

def confidence_refinement(state: FinancialGraphState) -> dict:
    # For local version we skip heavy refinement; just copy answers
    answers = state.get("answers", [])
    return {"refined_answers": answers, "errors": state.get("errors", [])}
