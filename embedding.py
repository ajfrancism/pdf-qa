import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)
    return embeddings


def retrieve(query, embeddings, chunks, k=3):
    query_embedding = model.encode([query])[0]

    # cosine similarity
    similarities = np.dot(embeddings, query_embedding) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_embedding)
    )

    top_k_indices = np.argsort(similarities)[-k:][::-1]

    return [chunks[i] for i in top_k_indices]