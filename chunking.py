#Fixed-size chunking
def fixed_chunking(pages, chunk_size=500, overlap=100):
    chunks = []

    for page in pages:
        text = page["text"]
        start = 0
        chunk_id = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "text": chunk_text,
                "page": page["page"],
                "chunk_id": chunk_id
            })

            start += chunk_size - overlap
            chunk_id += 1

    return chunks


#Paragraph-based chunking
def paragraph_chunking(pages):
    chunks = []
    chunk_id = 0  # ✅ global counter

    for page in pages:
        paragraphs = page["text"].split("\n\n")

        for para in paragraphs:
            if para.strip():
                chunks.append({
                    "text": para.strip(),
                    "page": page["page"],
                    "chunk_id": chunk_id
                })
                chunk_id += 1  # ✅ increment globally

    return chunks