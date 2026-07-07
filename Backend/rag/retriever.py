from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

def retrieve(query):

    retrieved_docs = vector_store.similarity_search(
        query,
        k=5
    )

    results = []

    for doc in retrieved_docs:

        results.append({

            "content": doc.page_content,

            "source": doc.metadata.get("source"),

            "page": doc.metadata.get("page")
        })

    return results