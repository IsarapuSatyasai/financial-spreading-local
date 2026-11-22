"""Parse PDF using local PyMuPDF."""
from src.graph.graph_state import FinancialGraphState
from utils.pdf_parser import parse_pdf_local

def parse_pdf(state: FinancialGraphState) -> dict:
    pdf_source = state.get("pdf_source")
    try:
        pages = parse_pdf_local(pdf_source)
        return {"pdf_pages": pages, "errors": state.get("errors", [])}
    except Exception as e:
        return {
            "pdf_pages": [],
            "errors": state.get("errors", []) + [f"PDF parse error: {str(e)}"],
        }
