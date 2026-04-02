from pdf_utils import extract_text_from_pdf
from chunking import fixed_chunking, paragraph_chunking
from embedding import create_embeddings, build_faiss_index, retrieve
from generator import generate_answer

pdf_path = "sample.pdf"

#Extract text
pages = extract_text_from_pdf(pdf_path)
print(f"Extracted {len(pages)} pages")

#Chunking
fixed_chunks = fixed_chunking(pages)
para_chunks = paragraph_chunking(pages)

print(f"Fixed chunks: {len(fixed_chunks)}")
print(f"Paragraph chunks: {len(para_chunks)}")

# Show sample
print("\nSample chunk:")
print(fixed_chunks[0])

#Create embeddings
embeddings = create_embeddings(fixed_chunks)

#Build FAISS index
index = build_faiss_index(embeddings)

#Query test
query = "What qualifications are required for this role?"

results = retrieve(query, index, fixed_chunks)

print("\nTop results:")
for r in results:
    print(f"\nPage {r['page']} | Chunk {r['chunk_id']}")
    print(r["text"])  
#[:200]) if I need to preview just the first 200 chars of the text
          
# Step 6: Generate answer
answer = generate_answer(query, results)

print("\nFinal Answer:\n")
print(answer)