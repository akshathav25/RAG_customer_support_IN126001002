from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq

from retriever import get_retriever
from hitl import escalate_to_human
from config import GROQ_API_KEY, LLM_MODEL


class GraphState(TypedDict):
    query: str
    context: str
    answer: str
    needs_human: bool


retriever = get_retriever()

llm = ChatGroq(
    model=LLM_MODEL,
    temperature=0,
    groq_api_key=GROQ_API_KEY
)

sensitive_keywords = [
    "billing",
    "suspension",
    "enterprise",
    "legal",
    "compliance",
    "fraud",
    "security",
    "contract",
    "payment failure",
    "account blocked"
]

def process_query(state):
    query = state["query"].lower()

    # Step 0: Sensitive issue check
    for keyword in sensitive_keywords:
        if keyword in query:
            return {
                "query": query,
                "context": "",
                "answer": "",
                "needs_human": True
            }
     # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: If no docs found → escalate
    if not docs:
        return {
            "query": query,
            "context": "",
            "answer": "",
            "needs_human": True
        }
     # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: If no docs found → escalate
    if not docs:
        return {
            "query": query,
            "context": "",
            "answer": "",
            "needs_human": True
        }

    # Step 1: Retrieve relevant documents
    docs = retriever.invoke(query)

    # Step 2: If no docs found → escalate
    if not docs:
        return {
            "query": query,
            "context": "",
            "answer": "",
            "needs_human": True
        }

    # Step 3: Create context
    context = "\n".join(
        [doc.page_content for doc in docs]
    )
    
    prompt = f"""
You are a professional customer support assistant.

Your job is to answer customer questions ONLY using the provided context.

Strict Rules:
1. Do NOT make up answers
2. Do NOT use outside knowledge
3. If the answer is missing, unclear, or incomplete,
   reply ONLY with:
   ESCALATE
4. Keep answers short, clear, and professional
5. If the issue is sensitive (billing, compliance, suspension),
   prefer escalation over guessing

Context:
{context}

User Question:
{query}
"""

    response = llm.invoke(prompt)
    answer = response.content

    if "ESCALATE" in answer.upper():
        return {
            "query": query,
            "context": context,
            "answer": "",
            "needs_human": True
        }

    return {
        "query": query,
        "context": context,
        "answer": answer,
        "needs_human": False
    }


def human_node(state):
    human_answer = escalate_to_human(
        state["query"]
    )

    return {
        "query": state["query"],
        "context": state["context"],
        "answer": human_answer,
        "needs_human": False
    }


def route_decision(state):
    if state["needs_human"]:
        return "human"

    return "end"


builder = StateGraph(GraphState)

builder.add_node("process", process_query)
builder.add_node("human", human_node)

builder.set_entry_point("process")

builder.add_conditional_edges(
    "process",
    route_decision,
    {
        "human": "human",
        "end": END
    }
)

builder.add_edge("human", END)

graph = builder.compile()