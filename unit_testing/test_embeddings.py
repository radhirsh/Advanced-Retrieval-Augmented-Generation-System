from Embeddings.Generate_Embeddings import generate_embed_query,generate_embeddings_for_documents



def test_embed_query():
    assert len(generate_embed_query("hi")) > 0



from Chunking.Document_Chunker import (
    chunk_documents
)

from Data_Ingestion.Document_Loader import (
    ingest_data
)


from Chunking.Document_Chunker import chunk_documents

def test_embeddings_documents():

    file_paths = [
        r"C:\Users\BRADSOL\Downloads\Sridhar_Files_Outsource\End_to_End_Rag\Policy_Documents\Access Card Policy.docx"
    ]

    documents = ingest_data(
        file_paths
    )

    chunks = chunk_documents(
        documents
    )

    generate_embeddings_for_documents(chunks)

    assert len(generate_embeddings_for_documents(chunks)) > 0