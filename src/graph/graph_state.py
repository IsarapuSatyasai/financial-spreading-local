"""Graph state for financial spreading (local)."""
from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict
from langchain_openai import ChatOpenAI

class Metric(TypedDict):
    worksheet: str
    variable: str
    description: str
    formula: Optional[str]
    remarks: Optional[str]

class FinancialGraphState(TypedDict, total=False):
    excel_path: str
    pdf_source: str
    output_path: str
    pdf_file_name: str
    excel_data: List[Metric]
    pdf_pages: List[Dict[str, Any]]
    source_language: str
    llm: Optional[ChatOpenAI]
    selected_pages: List[Dict[str, Any]]
    answers: List[Dict[str, Any]]
    refined_answers: List[Dict[str, Any]]
    errors: List[str]
    extraction_completed: bool
