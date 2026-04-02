# 📄 RAG-Based PDF Question Answering System

## 🚀 Overview
This project is an end-to-end Retrieval-Augmented Generation (RAG) system that allows users to upload a PDF and ask natural language questions about its content.

The system extracts text, chunks it into meaningful segments, retrieves relevant context, and generates grounded answers.

---

## 🧠 Architecture

PDF → Text Extraction → Chunking → Embeddings → Vector Search → LLM → Answer

---

## ⚙️ Features

- PDF text extraction using PyMuPDF
- Two chunking strategies:
  - Fixed-size chunking with overlap
  - Paragraph-based chunking
- Metadata tracking (page number, chunk index, character offsets)
- Modular and extensible pipeline

---

## 📂 Project Structure
rag-project/
├── main.py
├── pdf_utils.py
├── chunking.py
├── test_chunking.py
└── README.md

---

## 🔍 Chunking Strategies

### 1. Fixed Chunking
- Splits text into fixed-size segments
- Uses overlap to preserve context

### 2. Paragraph Chunking
- Splits text based on paragraph boundaries
- Preserves semantic meaning

---

## 🧪 Testing

Basic unit tests are implemented to validate chunking logic.

Run tests using: pytest


---

## ⚡ How to Run
python main.py


---

## 🛠️ Tech Stack

- Python
- PyMuPDF
- FastAPI (upcoming)
- FAISS (upcoming)
- Sentence Transformers (upcoming)

---

## 📌 Future Improvements

- Add embeddings and vector search
- Implement question answering using LLM
- Build API and frontend interface
- Deploy to public URL

---

## 🧠 Notes

This project is part of a technical assessment focusing on building an end-to-end AI system with strong emphasis on engineering quality, experimentation, and documentation.