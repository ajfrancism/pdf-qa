import streamlit as st
from pdf_utils import extract_text_from_pdf
from chunking import paragraph_chunking  # ✅ use paragraph chunking
from embedding import create_embeddings, retrieve
from generator import generate_answer
import tempfile

st.set_page_config(page_title="📄 PDF Q&A System", layout="wide")

st.title("📄 RAG PDF Question Answering")

# -----------------------------
# Upload PDF
# -----------------------------
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None:
    # Save file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    st.success("PDF uploaded successfully!")

    # -----------------------------
    # Process PDF
    # -----------------------------
    pages = extract_text_from_pdf(file_path)

    # ✅ Use paragraph chunking (fixes broken words)
    chunks = paragraph_chunking(pages)

    embeddings = create_embeddings(chunks)

    # Store in session
    st.session_state["embeddings"] = embeddings
    st.session_state["chunks"] = chunks

    st.info("Document processed. You can now ask questions!")

# -----------------------------
# Ask Question
# -----------------------------
query = st.text_input("Ask a question about the document")

if query and "index" in st.session_state:
   retrieved = retrieve(
    query,
    st.session_state["embeddings"],
    st.session_state["chunks"]
)

    # -----------------------------
    # Show Retrieved Context (Clean UI)
    # -----------------------------
st.subheader("📄 Retrieved Context")

for r in retrieved:
        with st.expander(f"Page {r['page']} | Chunk {r['chunk_id']}"):
            st.write(r["text"])  # ✅ full text (no truncation)

    # -----------------------------
    # Generate Answer
    # -----------------------------
answer = generate_answer(query, retrieved)

st.subheader("💬 Answer")
st.write(answer)