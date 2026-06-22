from langchain_community.vectorstores import FAISS

def build_vector_store(chunks, embeddings):

    return FAISS.from_documents(
        chunks,
        embeddings
    )