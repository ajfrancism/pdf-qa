# RAG PDF Question Answering System

An end-to-end Retrieval-Augmented Generation (RAG) system that enables users to upload PDFs and query them using natural language.

Built as part of an AI Research Engineer Internship assessment, this project demonstrates document understanding, semantic retrieval, and grounded answer generation using modern LLM workflows.

---

## 🌐 Live Demo

[Live Demo](https://pdf-app-atticai.streamlit.app/)

---

## Features

- Upload PDF documents (up to 20 pages)
- Extract structured text using PyMuPDF
- Semantic chunking (paragraph-based)
- Embedding generation using Sentence Transformers
- Similarity-based retrieval (cosine similarity)
- LLM-powered answer generation (OpenAI)
- Transparent retrieval (view source chunks)

---

## How It Works

1. **PDF Upload**
   - User uploads a document via Streamlit UI

2. **Text Extraction**
   - Extracts text page-by-page using PyMuPDF

3. **Chunking**
   - Splits text into semantically meaningful paragraphs

4. **Embedding**
   - Converts chunks into vector representations using `all-MiniLM-L6-v2`

5. **Retrieval**
   - Computes cosine similarity between query and chunks
   - Returns top-k relevant chunks

6. **Answer Generation**
   - Uses OpenAI model to generate grounded answers
   - Ensures responses are based only on retrieved context

---

## Design Decisions

### 🔹 Chunking Strategy
- Implemented **paragraph-based chunking** to preserve semantic meaning
- Avoids sentence truncation issues seen in fixed-size chunking

### 🔹 Retrieval Method
- Used **NumPy cosine similarity** instead of FAISS
- Chosen for **deployment compatibility (Python 3.14)** and simplicity

### 🔹 Hallucination Control
- Prompt explicitly restricts model to provided context
- Returns fallback if answer is not found

### 🔹 Transparency
- Displays retrieved chunks in UI for interpretability

---

## Limitations

- Dependent on OpenAI API (cost + rate limits)
- PDF formatting can affect extraction quality
- No multi-document support yet

---

## Tech Stack

- Python
- Streamlit
- PyMuPDF
- Sentence Transformers
- NumPy
- OpenAI API

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/yourusername/pdf-qa.git
cd pdf-qa
pip install -r requirements.txt
streamlit run app.py

## Environment Variables
 Set your API key locally:

### Windows
setx OPENAI_API_KEY "your-api-key"

## Mac OS / Linux 
export OPENAI_API_KEY="your-api-key"

Note: Never commit your API keys to version control. Use environment variables or Streamlit Secrets instead.

## 🧠 Key Insight

This project highlights the importance of chunking strategy and retrieval quality in RAG systems. Small design decisions—such as paragraph-based chunking or similarity computation—significantly impact answer accuracy and user experience.