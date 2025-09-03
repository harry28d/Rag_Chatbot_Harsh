# from langchain.document_loaders import PyMuPDFLoader, TextLoader, Docx2txtLoader
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from vector_store import save_vector_store



def load_documents(directory: str):
    all_docs = []

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if filename.endswith(".pdf"):
            loader = PyMuPDFLoader(filepath)
        elif filename.endswith(".docx"):
            loader = Docx2txtLoader(filepath)
        elif filename.endswith(".txt"):
            loader = TextLoader(filepath)
        else:
            print(f"Skipped unsupported file: {filename}")
            continue

        docs = loader.load()
        for doc in docs:
            doc.metadata["source"] = filepath

        all_docs.extend(docs)

    return all_docs
docs = load_documents("data/")
print(f"Loaded {len(docs)} documents")


def chunk_documents(documents, chunk_size=300, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    return splitter.split_documents(documents)

chunks = chunk_documents(docs)
print(f"Generated {len(chunks)} chunks")

if __name__ == "__main__":
    docs = load_documents("data/")
    chunks = chunk_documents(docs)
    save_vector_store(chunks, persist_path="docs/faiss_index")
