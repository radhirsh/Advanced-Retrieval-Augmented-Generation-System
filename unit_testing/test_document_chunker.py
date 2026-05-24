from Chunking.Document_Chunker import (
    chunk_documents
)

from Data_Ingestion.Document_Loader import (
    ingest_data
)


def test_chunk_documents():

    file_paths = [
        r"C:\Users\BRADSOL\Downloads\Sridhar_Files_Outsource\End_to_End_Rag\Policy_Documents\Access Card Policy.docx"
    ]

    documents = ingest_data(
        file_paths
    )

    chunks = chunk_documents(
        documents
    )

    assert len(chunks) > 0