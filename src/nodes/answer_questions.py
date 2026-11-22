"""Answer questions / extract metrics using LLM (simplified local)."""
import json
from langchain_core.messages import SystemMessage, HumanMessage
from src.graph.graph_state import FinancialGraphState
from src.prompts.system_prompt import SYSTEM_PROMPT
from src.prompts.user_prompt import get_user_prompt
from src.models import ExtractionResponse

def answer_questions(state: FinancialGraphState) -> dict:
    llm = state.get("llm")
    metrics = state.get("excel_data", [])
    pages = state.get("selected_pages", [])

    if not llm or not metrics or not pages:
        return {"answers": [], "errors": state.get("errors", []) + ["Missing LLM, metrics or pages"]}

    try:
        page_text = "\n\n".join(
            f"--- Page {p.get('page_number', '?')} ---\n{p.get('text', '')}"
            for p in pages[:15]
        )
        user_prompt = get_user_prompt(metrics)
        full_prompt = f"{user_prompt}\n\n## Document content:\n{page_text[:15000]}"

        structured_llm = llm.with_structured_output(ExtractionResponse)
        result = structured_llm.invoke([
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=full_prompt),
        ])

        answers = [a.model_dump() for a in result.answers]
        return {"answers": answers, "errors": state.get("errors", [])}
    except Exception as e:
        return {"answers": [], "errors": state.get("errors", []) + [f"Extraction error: {str(e)}"]}
