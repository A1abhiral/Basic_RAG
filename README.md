 What I Learned While Building This Project
 
1. How RAG Works Internally

While building this system, I deeply understood the full Retrieval-Augmented Generation (RAG) pipeline:
Document ingestion (PDF / text loading)
Semantic chunking
Embedding generation
Vector database storage
Similarity search
Context injection into prompt
LLM-based answer generation

2. Vector Embeddings & Similarity Search

I learned:
How text is converted into numerical vector representations
How cosine similarity retrieves semantically relevant chunks
Why embedding models differ from generative LLMs
Trade-offs between local embeddings and API-based embeddings

3. Vector Databases (Chroma vs FAISS vs Pinecone)

Through experimentation, I understood:
Local persistence using Chroma
How vector indexing works
Differences between local vector stores and managed cloud solutions
When to use each in production systems
