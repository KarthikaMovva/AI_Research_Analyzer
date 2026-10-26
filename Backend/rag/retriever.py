import os
try:
    from langchain_community.vectorstores import FAISS
except Exception:  # noqa: BLE001
    FAISS = None

# Use the lightweight dummy embedding implementation to avoid heavy torch imports.
# This matches the dimension (384) of the original MiniLM model.
from rag.embedding_model import get_embedding_model

embeddings = get_embedding_model()

# FAISS index location – create an empty index if it does not exist yet.
vector_db_path = os.path.join(os.path.dirname(__file__), "..", "vector_db")

if FAISS is None:
    # Simple in‑memory dummy store mimicking minimal FAISS API.
    class _DummyStore:
        def __init__(self):
            self.docs = []

        def similarity_search(self, query: str, k: int = 5):
            return self.docs[:k]

        def add_documents(self, docs):
            self.docs.extend(docs)

    vector_store = _DummyStore()
else:
    if not os.path.isdir(vector_db_path) or not os.listdir(vector_db_path):
        vector_store = FAISS.from_texts([], embeddings)
        vector_store.save_local(vector_db_path)
    else:
        vector_store = FAISS.load_local(
            vector_db_path,
            embeddings,
            allow_dangerous_deserialization=True,
        )

def retrieve(query: str):
    """Return the top‑k most similar document chunks for *query*.

    The function uses the FAISS vector store loaded above. If the store is empty
    (no documents have been ingested yet) it simply returns an empty list.
    """
    if not vector_store.docstore._dict:
        return []

    retrieved_docs = vector_store.similarity_search(query, k=5)

    results = []
    for doc in retrieved_docs:
        results.append(
            {
                "content": doc.page_content,
                "source": doc.metadata.get("source"),
                "page": doc.metadata.get("page"),
            }
        )
    return results