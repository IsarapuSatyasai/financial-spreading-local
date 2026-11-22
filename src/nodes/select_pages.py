"""Simple page selection (local). Takes first N pages or pages with financial keywords."""
from src.graph.graph_state import FinancialGraphState
from config import get_settings

def select_pages(state: FinancialGraphState) -> dict:
    settings = get_settings()
    pages = state.get("pdf_pages", [])
    if not pages:
        return {"selected_pages": [], "errors": state.get("errors", [])}

    keywords = ["balance sheet", "income statement", "profit and loss", "cash flow",
                "revenue", "assets", "liabilities", "equity", "notes to"]
    selected = []
    for p in pages[:settings.first_n_pages]:
        text = (p.get("text") or "").lower()
        if any(k in text for k in keywords) or len(selected) < 5:
            selected.append(p)
        if len(selected) >= settings.max_selected_pages:
            break

    if not selected:
        selected = pages[:min(10, len(pages))]

    return {"selected_pages": selected, "errors": state.get("errors", [])}
