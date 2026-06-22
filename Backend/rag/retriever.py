from rag.embedding_model import get_embedding_model
from rag.vector_store import load_vector_store

embeddings = get_embedding_model()

vector_store = load_vector_store(
    embeddings
)

def retrieve(query, k=3):

    return vector_store.similarity_search(
        query,
        k=k
    )