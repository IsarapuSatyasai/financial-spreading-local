"""Detect source language (local)."""
from langdetect import detect, DetectorFactory
from src.graph.graph_state import FinancialGraphState

DetectorFactory.seed = 0

def source_language(state: FinancialGraphState) -> dict:
    pages = state.get("pdf_pages", [])
    if not pages:
        return {"source_language": "English", "errors": state.get("errors", [])}
    try:
        sample = " ".join(p.get("text", "") for p in pages[:5])
        if len(sample) < 50:
            lang = "English"
        else:
            code = detect(sample)
            lang_map = {"en": "English", "nl": "Dutch", "de": "German", "fr": "French"}
            lang = lang_map.get(code, "English")
        return {"source_language": lang, "errors": state.get("errors", [])}
    except Exception as e:
        return {"source_language": "English", "errors": state.get("errors", []) + [str(e)]}
