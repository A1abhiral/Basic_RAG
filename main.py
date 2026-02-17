from document_pipeline import load_documents, chunk_documents
from vector_store import create_vector_store, load_vector_store
from rag_chain import create_rag_chain
import os


if not os.path.exists("./chroma_db"):
    docs = load_documents("physics.pdf")
    chunks = chunk_documents(docs)
    vectorstore = create_vector_store(chunks)
else:
    vectorstore = load_vector_store()

qa_chain = create_rag_chain(vectorstore)

while True:
    query = input("Ask: ")
    if query.lower() == "exit":
        break

    result = qa_chain(query)
    print("\nAnswer:\n", result["answer"])

