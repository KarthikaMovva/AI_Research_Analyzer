from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
try:
    from langchain_community.vectorstores import FAISS
except Exception:  # noqa: BLE001
    FAISS = None

# Use lightweight dummy embeddings (no torch dependency)
from rag.embedding_model import get_embedding_model

from rag.document_loader import load_document


UPLOAD_FOLDER = "uploads"
VECTOR_DB_PATH = "vector_db"



embeddings = get_embedding_model()



def build_vector_store(file_path):


    # 1. Load only newly uploaded file

    documents = load_document(
        file_path
    )


    # 2. Chunk document

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )


    chunks = splitter.split_documents(
        documents
    )


    # 3. Check existing vector DB

    vector_db = Path(
        VECTOR_DB_PATH
    )


    if vector_db.exists():

        vector_store = FAISS.load_local(
            VECTOR_DB_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )


        vector_store.add_documents(
            chunks
        )


    else:

        vector_store = FAISS.from_documents(
            chunks,
            embeddings
        )


    # 4. Save updated index

    vector_store.save_local(
        VECTOR_DB_PATH
    )


    return len(chunks)