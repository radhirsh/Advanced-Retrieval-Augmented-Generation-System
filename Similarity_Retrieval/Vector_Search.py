from Vector_Database.Milvus_Vector_DB import vector_store
from Embeddings.Generate_Embeddings import Embedding_Client
from libraries import *

COLLECTION_NAME = "rag_collection"

def vector_search(query, top_k=25):

    try:

        # Ensure query is string
        if isinstance(query, list):
            query = " ".join(query)

        query = str(query).strip()

        vector_store.load_collection(
            collection_name=COLLECTION_NAME
        )

        query_embedding = Embedding_Client.embed_query(query)

        results = vector_store.search(
            collection_name=COLLECTION_NAME,
            data=[query_embedding],
            limit=top_k,
            output_fields=["text"]
        )

        # retrieved_docs = [
        #     result["entity"]["text"]
        #     for result in results[0]
        # ]
        retrieved_docs = [
        Document(
            page_content=result["entity"]["text"]
        )
        for result in results[0]
    ]

        print(f"Retrieved {len(retrieved_docs)} chunks")

        return retrieved_docs

    except Exception as e:

        print("Vector Search Error")
        print(str(e))
        traceback.print_exc()

        return []