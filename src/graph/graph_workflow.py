"""LangGraph workflow (local)."""
from langgraph.graph import StateGraph, START, END
from src.graph.graph_state import FinancialGraphState
from src.nodes.read_template import read_template
from src.nodes.parse_pdf import parse_pdf
from src.nodes.source_language import source_language
from src.nodes.select_pages import select_pages
from src.nodes.connect_llm import connect_llm
from src.nodes.answer_questions import answer_questions
from src.nodes.confidence_refinement import confidence_refinement
from src.nodes.create_excel_output import create_excel_output

def complete(state: FinancialGraphState) -> dict:
    return {"extraction_completed": True}

def build_graph():
    workflow = StateGraph(FinancialGraphState)

    workflow.add_node("read_template", read_template)
    workflow.add_node("parse_pdf", parse_pdf)
    workflow.add_node("source_language", source_language)
    workflow.add_node("select_pages", select_pages)
    workflow.add_node("connect_llm", connect_llm)
    workflow.add_node("answer_questions", answer_questions)
    workflow.add_node("confidence_refinement", confidence_refinement)
    workflow.add_node("create_excel_output", create_excel_output)
    workflow.add_node("complete", complete)

    workflow.add_edge(START, "read_template")
    workflow.add_edge("read_template", "parse_pdf")
    workflow.add_edge("parse_pdf", "source_language")
    workflow.add_edge("source_language", "select_pages")
    workflow.add_edge("select_pages", "connect_llm")
    workflow.add_edge("connect_llm", "answer_questions")
    workflow.add_edge("answer_questions", "confidence_refinement")
    workflow.add_edge("confidence_refinement", "create_excel_output")
    workflow.add_edge("create_excel_output", "complete")
    workflow.add_edge("complete", END)

    return workflow.compile()
