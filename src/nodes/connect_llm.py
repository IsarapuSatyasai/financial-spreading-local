"""Connect to OpenAI (local ChatOpenAI)."""
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from config import get_settings
from src.graph.graph_state import FinancialGraphState

def connect_llm(state: FinancialGraphState) -> dict:
    settings = get_settings()
    try:
        llm = ChatOpenAI(
            model=settings.openai_model,
            temperature=settings.temperature,
            api_key=settings.openai_api_key,
        )
        # Quick connectivity check
        llm.invoke([HumanMessage(content="ping")])
        return {"llm": llm, "errors": state.get("errors", [])}
    except Exception as e:
        return {
            "llm": None,
            "errors": state.get("errors", []) + [f"LLM connection error: {str(e)}"],
        }
