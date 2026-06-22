from rag.document_loader import load_pdf
from rag.chunker import create_chunks
from rag.embedding_model import get_embedding_model
from rag.vector_store import (
    build_vector_store,
    save_vector_store
)

docs = load_pdf(
    "Data/RAG_Explanation.pdf"
)

chunks = create_chunks(docs)

embeddings = get_embedding_model()

vector_store = build_vector_store(
    chunks,
    embeddings
)

save_vector_store(
    vector_store
)

print("Index Saved")