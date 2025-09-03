from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from vector_store import load_vector_store
from dotenv import load_dotenv
from document_loader import load_documents, chunk_documents
from vector_store import load_vector_store, save_vector_store, faiss_index_exists 


load_dotenv()  # loads OPENAI_API_KEY

def run_rag_query(user_query: str):
    persist_path = "docs/faiss_index"

    if not faiss_index_exists(persist_path):
        print("[INFO] FAISS index not found. Rebuilding...")
        docs = load_documents("data/")
        chunks = chunk_documents(docs)
        save_vector_store(chunks, persist_path)

    vector_store = load_vector_store(persist_path)

    retriever = vector_store.as_retriever(
        search_type="similarity", search_kwargs={"k": 3}
    )

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an intelligent assistant. Use the following context to answer the question.
Include source filenames wherever relevant in your answer.

Context:
{context}

Question:
{question}

Answer (with sources):
"""
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt_template}
    )

    result = qa_chain.invoke(user_query)

    # ✅ Debug: Print retrieved chunks
    print("\n🔍 Retrieved Chunks:\n")
    for i, doc in enumerate(result["source_documents"]):
        print(f"--- Chunk {i+1} from {doc.metadata.get('source', 'unknown')} ---")
        print(doc.page_content[:300], "\n")

    answer = result["result"]
    sources = result["source_documents"]
    citations = set(doc.metadata.get("source", "unknown") for doc in sources)

    return answer, citations  # ✅ Important: return both
