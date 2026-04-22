from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import CHROMA_PATH, EMBEDDING_MODEL


def get_retriever():
    # Step 1: Load embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    # Step 2: Connect to existing ChromaDB
    vectorstore = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embeddings
    )

    # Step 3: Create retriever
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever