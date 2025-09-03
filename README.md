# 💬 RAG Chatbot — AI Assistant Powered by LangChain, FAISS, and Streamlit

[![🚀 Live Demo](https://img.shields.io/badge/%F0%9F%9A%80%20Live%20Demo-Streamlit-brightgreen?style=for-the-badge)](https://ragchatbotharsh28d.streamlit.app/)

---

## 📌 Overview

This is a **Retrieval-Augmented Generation (RAG)** based chatbot built using:

- **LangChain** for chaining components (retriever + LLM)
- **FAISS** for semantic vector search
- **Sentence Transformers** for high-quality embeddings
- **Streamlit** for a simple, clean web UI
- **OpenAI GPT-3.5** as the LLM backend

It reads your documents (PDF, DOCX, TXT), indexes them, and answers your questions using the most relevant chunks — with proper source citations.

---

## 🧠 What This Project Does

✔️ Ingests documents from the `data/` folder  
✔️ Splits them into semantic chunks  
✔️ Embeds them using `multi-qa-MiniLM-L6-cos-v1`  
✔️ Stores vectors in FAISS index  
✔️ Uses LangChain RAG pipeline to answer questions  
✔️ Displays source file citations  
✔️ Rebuilds the FAISS index automatically if missing  
✔️ Web interface powered by Streamlit  
✔️ Feedback buttons included (👍 / 👎)

---

## 📚 On What Document it is trained on  (Training Documents)

The chatbot is trained on a collection of documents stored in the `/data/` folder:

| 📄 Document Name         | Description                                             |
|--------------------------|---------------------------------------------------------|
| `Langchain.pdf`          | Covers the LangChain framework, its modules, and how it facilitates chaining LLM components for structured tasks. |
| `OpenAI.pdf`             | Provides introductory knowledge about OpenAI, its capabilities, models, and use cases. |
| `Python Tutorial.docx`   | A comprehensive tutorial on Python fundamentals, OOP concepts, and class-based structures. |
| `Transformer.pdf`        | Explains the Transformer architecture, its layers, attention mechanism, and relevance in LLMs. |

---

## ⚙️ Tech Stack

| Component        | Technology                        |
|------------------|-----------------------------------|
| 🔄 RAG Pipeline  | `LangChain`                       |
| 🔎 Vector DB     | `FAISS`                           |
| 🧠 Embeddings     | `Sentence-Transformers` (multi-qa-MiniLM-L6-cos-v1) |
| 🤖 LLM           | `OpenAI GPT-3.5 Turbo`            |
| 📄 Document Load | `PyMuPDF`, `docx2txt`, `TextLoader` |
| 🌐 Web UI        | `Streamlit`                       |
| 🔐 Secrets Mgmt  | `.env` with `python-dotenv`       |

---

## 🧪 Example Questions

- What is LangChain?
- What are the core concepts of Transformers?
- What is polymorphism in Python?
- Summarize OpenAI's features

---

## 🚀 How to Run Locally

### 🔧 1. Clone the repo

```bash
git clone https://github.com/harry28d/Rag_Chatbot_Harsh
cd rag-chatbot
