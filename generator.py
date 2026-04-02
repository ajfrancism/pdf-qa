from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_answer(query, retrieved_chunks):
    """
    Generates an answer using retrieved context.

    Args:
        query (str): User question
        retrieved_chunks (list): Relevant chunks

    Returns:
        str: Generated answer
    """

    # Combine retrieved chunks into context
    context = "\n\n".join([
    f"[Page {chunk['page']} | Chunk {chunk['chunk_id']}]\n{chunk['text']}"
    for chunk in retrieved_chunks
])

    # Prompt with hallucination control
    prompt = f"""
You are an AI assistant answering questions based ONLY on the provided context.

If the answer is not found in the context, say:
"I don't know based on the document."

Always cite the page number when possible.

Context:
{context}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # cheaper + fast
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    return response.choices[0].message.content