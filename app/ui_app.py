import streamlit as st
from rag_engine import run_rag_query

st.set_page_config(page_title="RAG Chatbot", page_icon="💬")

st.title("📚 RAG Chatbot")
st.write("Ask any question based on the uploaded documents.")

query = st.text_input("🔎 Enter your question")

if query:
    with st.spinner("🤖 Generating answer..."):
        try:
            answer, citations = run_rag_query(query)
            st.success("✅ Answer generated")

            st.markdown("### 📌 Answer")
            st.write(answer)

            st.markdown("### 📄 Sources")
            for src in citations:
                st.code(src)

            st.markdown("### 👍 Feedback")
            col1, col2 = st.columns(2)
            with col1:
                if st.button("👍 Helpful"):
                    st.success("Thanks for your feedback!")
            with col2:
                if st.button("👎 Not Helpful"):
                    st.warning("Thanks! We'll use this to improve.")

        except Exception as e:
            st.error(f"❌ Error: {e}")
