from libraries import *

from Embeddings.Generate_Embeddings import (
    Embedding_Client
)

URI = (
    "./Vector_Database/milvus_demo.db"
)

COLLECTION_NAME = (
    "rag_collection"
)


def initialize_milvus():

    try:

        os.makedirs(
            "Vector_Database",
            exist_ok=True
        )

        client = MilvusClient(
            uri=URI
        )

        existing_collections = (
            client.list_collections()
        )

        # -------------------
        # Create Collection
        # If Not Exists
        # -------------------
        if (
            COLLECTION_NAME
            not in existing_collections
        ):

            embedding_dim = len(

                Embedding_Client
                .embed_query(
                    "sample"
                )
            )

            client.create_collection(

                collection_name=COLLECTION_NAME,
                dimension=embedding_dim,
                metric_type="COSINE"

            )

            print(
                f"Collection "
                f"'{COLLECTION_NAME}' "
                f"created "
                f"successfully"
            )

        else:

            print(
                f"Collection "
                f"'{COLLECTION_NAME}' "
                f"already exists"
            )

        print(
            "Milvus initialized "
            "successfully"
        )

        return client

    except Exception as e:

        print(
            "Milvus "
            "Initialization Error:",
            str(e)
        )

        traceback.print_exc()

        return None


vector_store = (
    initialize_milvus()
)