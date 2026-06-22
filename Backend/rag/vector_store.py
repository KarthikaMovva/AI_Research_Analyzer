from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, embeddings):

    return FAISS.from_documents(
        chunks,
        embeddings
    )

def save_vector_store(vector_store):

    vector_store.save_local(
        "vector_db"
    )

def load_vector_store(embeddings):

    return FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )