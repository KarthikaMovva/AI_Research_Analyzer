from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)


def load_document(file_path):

    extension = Path(file_path).suffix.lower()


    if extension == ".pdf":

        loader = PyPDFLoader(file_path)


    elif extension == ".txt":

        loader = TextLoader(
            file_path,
            encoding="utf-8"
        )


    elif extension == ".docx":

        loader = Docx2txtLoader(
            file_path
        )


    else:

        raise Exception(
            f"Unsupported file type: {extension}"
        )


    return loader.load()


def load_pdf(file_path):
    """Convenience wrapper for loading PDFs. Mirrors the old public API used in tests."""
    if Path(file_path).suffix.lower() != ".pdf":
        raise Exception("load_pdf expects a .pdf file")
    return load_document(file_path)