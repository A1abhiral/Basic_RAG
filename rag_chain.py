from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


def create_rag_chain(vectorstore):

    llm = ChatOllama(
        model="mistral",
        temperature=0
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    prompt = ChatPromptTemplate.from_template("""
You are an AI assistant. Use the context below to answer the question.

Context:
{context}

Question:
{question}

Answer:
""")

    def rag_pipeline(question: str):

        # ✅ NEW API
        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        formatted_prompt = prompt.format(
            context=context,
            question=question
        )

        response = llm.invoke(formatted_prompt)

        return {
            "answer": response.content,
            "source_documents": docs
        }

    return rag_pipeline
