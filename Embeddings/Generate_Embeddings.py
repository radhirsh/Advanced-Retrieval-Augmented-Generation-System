from libraries import *
Embedding_Client=NVIDIAEmbeddings(
    model=os.getenv("NVIDIA_EMBEDDING_MODEL"),
    nvidia_api_key=os.getenv("NVIDIA_EMBEDDINGS_KEY")
)


def  generate_embeddings_for_documents(all_chunked_documents):
    all_embeddings=[]
    list_of_texts=[i.page_content for i in all_chunked_documents ]
    all_embeddings = (
            Embedding_Client.embed_documents(
                list_of_texts
            )
        )
    return all_embeddings



def generate_embed_query(query):
    return (Embedding_Client.embed_query(query))