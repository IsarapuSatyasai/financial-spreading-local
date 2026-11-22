"""Simple local PDF parser using PyMuPDF."""
import fitz  # pymupdf
from pathlib import Path

def parse_pdf_local(pdf_path: str | Path) -> list:
    """Return list of {page_number, text} dicts."""
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc, start=1):
        text = page.get_text("text")
        pages.append({"page_number": i, "text": text})
    doc.close()
    return pages
