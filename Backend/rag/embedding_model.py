import numpy as np

class DummyEmbeddings:
    """Lightweight embedding class to avoid heavy dependencies.
    Returns zero vectors of dimension 384, matching the MiniLM model size.
    """
    def embed_query(self, text: str):
        return np.zeros(384, dtype="float32")

    def embed_documents(self, texts):
        return [np.zeros(384, dtype="float32") for _ in texts]

    def __call__(self, texts):
        """Make DummyEmbeddings callable for FAISS.

        If a list or tuple of texts is provided, embed each document; otherwise treat as a single query string.
        """
        if isinstance(texts, (list, tuple)):
            return self.embed_documents(texts)
        return self.embed_query(texts)

# Duplicate __call__ method removed

def get_embedding_model():
    """Return a dummy embeddings instance used by FAISS.
    This replaces the heavy HuggingFaceEmbeddings which pulls in torch.
    """
    return DummyEmbeddings()