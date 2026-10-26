#!/usr/bin/env python
import os, tempfile
from rag.embedding_model import get_embedding_model
from rag.ingestion import build_vector_store

def main():
    # Verify embedding model is callable
    embed = get_embedding_model()
    print('Embedding model callable?', callable(embed))
    # Create a temporary text file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.txt', mode='w', encoding='utf-8') as f:
        f.write('Hello world. This is a test document for ingestion.')
        tmp_path = f.name
    print('Temp file created at:', tmp_path)
    # Run ingestion to build vector store and get chunk count
    chunk_count = build_vector_store(tmp_path)
    print('Number of chunks created:', chunk_count)
    # Cleanup temp file
    os.remove(tmp_path)

if __name__ == '__main__':
    main()
