import streamlit as st
from graph import graph
from utils.helper import write_log


st.set_page_config(
    page_title="Customer Support Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Customer Support RAG Assistant")
st.write("Ask your customer support questions below.")

query = st.text_input(
    "Enter your question:"
)

if st.button("Get Answer"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        result = graph.invoke({
            "query": query,
            "context": "",
            "answer": "",
            "needs_human": False
        })

        st.subheader("Final Response")
        st.success(result["answer"])

        if result["needs_human"]:
            st.error("Escalated to Human Support")
        else:
            st.info("Resolved by AI Assistant")

        write_log(
            query=query,
            answer=result["answer"],
            escalated=result["needs_human"]
        )