from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load embedding model (lightweight and fast)
model = SentenceTransformer('all-MiniLM-L6-v2')


def create_embeddings(chunks):
    """
    Converts chunk text into vector embeddings.

    Args:
        chunks (list): List of chunk dictionaries

    Returns:
        np.array: Embeddings matrix
    """
    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)

    return embeddings


def build_faiss_index(embeddings):
    """
    Builds a FAISS index from embeddings.

    Args:
        embeddings (np.array): Embedding vectors

    Returns:
        faiss.Index: FAISS index
    """
    dimension = embeddings.shape[1]

    # Create FAISS index using L2 distance
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to index
    index.add(embeddings)

    return index


def retrieve(query, index, chunks, k=3):
    """
    Retrieves top-k relevant chunks based on a query.

    Args:
        query (str): User query
        index (faiss.Index): FAISS index
        chunks (list): Original chunk list
        k (int): Number of results to return

    Returns:
        list: Top-k relevant chunks
    """
    # Convert query into embedding
    query_embedding = model.encode([query])

    # Search FAISS index
    distances, indices = index.search(query_embedding, k)

    # Retrieve corresponding chunks
    results = [chunks[i] for i in indices[0]]

    return results