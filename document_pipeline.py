from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from pathlib import Path


def load_documents(path: str):
    path = Path(path)
    
    if path.suffix == ".pdf":
        loader = PyPDFLoader(path)
    elif path.suffix == ".txt":
        loader = TextLoader(path)
    else:
        raise ValueError("Unsupported file type")
    
    documents = loader.load()
    return documents


def chunk_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,
)

    docs = splitter.split_documents(documents)
    return docs
