from langchain_nvidia_ai_endpoints import NVIDIARerank
reranker = NVIDIARerank(
    nvidia_api_key="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"
)




def re_rank_documents(retrieved_chunks, query):
    reranked_docs = reranker.compress_documents(
        documents=retrieved_chunks,
        query=query
    )
    return reranked_docs

    