# RAG-Based Customer Support Assistant

## Project Overview

This project is a Retrieval-Augmented Generation (RAG) based Customer Support Assistant built using LangGraph and Human-in-the-Loop (HITL) escalation.

The system processes a PDF knowledge base, stores embeddings in ChromaDB, retrieves relevant information for user queries, and generates context-aware responses using an LLM through Groq.

If the system is not confident enough to answer, it escalates the query to human support instead of hallucinating.

This project demonstrates practical implementation of:

* RAG (Retrieval-Augmented Generation)
* Vector Database (ChromaDB)
* Embeddings using HuggingFace
* LangGraph workflow orchestration
* Conditional routing
* Human-in-the-Loop (HITL)
* Streamlit UI for interactive usage

---

## Problem Statement

Traditional chatbots often hallucinate and provide incorrect answers because they rely only on pretrained knowledge.

This project solves that problem by retrieving information directly from the company handbook PDF before generating responses.

This ensures:

* accurate answers
* reduced hallucination
* context-aware support
* safe handling of sensitive queries

---

## Features

* PDF knowledge base ingestion
* Automatic chunking of large documents
* Embedding generation using sentence transformers
* ChromaDB vector storage
* Semantic retrieval of relevant chunks
* Groq-powered LLM response generation
* LangGraph-based workflow management
* Conditional routing for sensitive queries
* Human escalation for low-confidence cases
* Logging of queries and responses
* Streamlit web interface

---

## Tech Stack

### Backend

* Python
* LangChain
* LangGraph
* ChromaDB
* Groq API
* HuggingFace Embeddings

### Frontend

* Streamlit

### Utilities

* PyPDF
* Python Dotenv
* Sentence Transformers

---

## Project Structure

```text
rag_customer_support/
│
├── app.py
├── streamlit_app.py
├── ingest.py
├── retriever.py
├── graph.py
├── hitl.py
├── config.py
├── requirements.txt
├── .env
├── logs.txt
│
├── data/
│   └── handbook.pdf
│
├── chroma_db/
│
└── utils/
    └── helper.py
```

---

## Workflow

```text
PDF → Load → Chunk → Embeddings → ChromaDB

User Query
→ Query Embedding
→ Similarity Search
→ Retrieve Relevant Chunks
→ LLM Response Generation
→ Confidence Check
→ AI Response OR Human Escalation
→ Final Output
```

---

## Installation

### Step 1: Clone Project

```bash
git clone <your-repository-link>
cd rag_customer_support
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Add Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### Step 4: Place PDF File

Put your handbook PDF inside:

```text
data/handbook.pdf
```

---

## Running the Project

## First Time Only

Generate embeddings:

```bash
python ingest.py
```

This creates the vector database.

---

## Run Terminal Version

```bash
python app.py
```

---

## Run Streamlit UI Version

```bash
streamlit run streamlit_app.py
```

Then open:

```text
http://localhost:8501
```

---

## Example Queries

* What is refund policy?
* Why was my account suspended?
* My enterprise billing failed
* What happens after failed payment retries?
* How are duplicate charges handled?

---

## Human-in-the-Loop (HITL)

The system escalates queries to human support when:

* no relevant chunks are found
* answer confidence is low
* LLM returns ESCALATE
* sensitive keywords are detected

Examples of sensitive queries:

* billing
* suspension
* enterprise
* legal
* compliance
* fraud

This prevents hallucination and improves trust.

---

## Why LangGraph?

LangGraph is used because real-world support systems require:

* stateful workflows
* conditional decisions
* routing logic
* escalation paths

Unlike simple chains, LangGraph supports production-style decision-making systems.

---

## Future Enhancements

* Multi-document support
* Chat history and memory
* Admin dashboard
* Feedback loop for continuous improvement
* Deployment using FastAPI + Docker
* Cloud deployment on AWS/GCP

---

## Conclusion

This project is not just a chatbot.

It is a scalable AI support system with decision-making capability.

By combining RAG, LangGraph, and HITL, the system provides accurate, safe, and production-ready customer support automation.

This makes it highly suitable for real-world enterprise support environments.
