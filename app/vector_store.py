import os
from langchain_community.vectorstores import FAISS
# from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path


def get_sentence_transformer_embedding(model_name="all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(model_name=model_name)

def save_vector_store(chunks, persist_path="docs/faiss_index"):
    embeddings = get_sentence_transformer_embedding()
    vector_store = FAISS.from_documents(chunks, embeddings)
    vector_store.save_local(persist_path)
    print(f"[INFO] FAISS vector store saved at: {persist_path}")
    return vector_store

def load_vector_store(persist_path="docs/faiss_index"):
    embeddings = get_sentence_transformer_embedding()
    # return FAISS.load_local(persist_path, embeddings)
    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)



def faiss_index_exists(persist_path="docs/faiss_index"):
    index_file = Path(persist_path) / "index.faiss"
    pkl_file = Path(persist_path) / "index.pkl"
    return index_file.exists() and pkl_file.exists()

