import sys
import os
import time
import traceback
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from libraries import *
from dotenv import load_dotenv

load_dotenv()

from Data_Ingestion.Document_Loader import ingest_data
from Data_Ingestion.Data_Monitor import data_monitor
from Chunking.Document_Chunker import chunk_documents
from Embeddings.Generate_Embeddings import generate_embeddings_for_documents
from Vector_Database.Milvus_Vector_DB import initialize_milvus
from Similarity_Retrieval.Vector_Search import vector_search
from Reranking.re_ranker import re_rank_documents
from LLM.Generate_Response import generate_response

documents_path = os.getenv("document_folder_path")


def rag_pipeline():

    start_time = time.time()

    # =====================================
    # 1. Monitor Files
    # =====================================

    try:
        monitored_files = data_monitor(documents_path)

        if not monitored_files:
            print("No new or modified files detected.")
            return

        print(f"Found {len(monitored_files)} files")

    except Exception as e:
        print("Error in Data Monitoring:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 2. Data Ingestion
    # =====================================

    try:
        documents = ingest_data(monitored_files)

        if not documents:
            print("No documents loaded.")
            return

        print(f"Loaded {len(documents)} documents")

    except Exception as e:
        print("Error in Data Ingestion:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 3. Chunking
    # =====================================

    try:
        chunked_documents = chunk_documents(documents)

        if not chunked_documents:
            print("No chunks created.")
            return

        print(f"Created {len(chunked_documents)} chunks")

    except Exception as e:
        print("Error in Document Chunking:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 4. Generate Embeddings
    # =====================================

    try:
        embeddings = generate_embeddings_for_documents(chunked_documents)

        if not embeddings:
            print("No embeddings generated.")
            return

        print(f"Generated {len(embeddings)} embeddings")

    except Exception as e:
        print("Error in Generating Embeddings:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 5. Initialize Milvus
    # =====================================

    try:
        VectorStore = initialize_milvus()

        if VectorStore is None:
            raise Exception("Milvus failed to initialize")

        try:
            VectorStore.drop_collection("rag_collection")
            print("Old collection deleted")

        except Exception:
            print("No old collection found")

        VectorStore = initialize_milvus()

        print("Milvus initialized successfully")

    except Exception as e:
        print("Error in Initializing Milvus:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 6. Prepare Data + Insert into Milvus
    # =====================================

    try:
        data = []
        excel_data = []

        for i, (chunk, embedding) in enumerate(zip(chunked_documents, embeddings)):

            try:

                if isinstance(embedding[0], list):
                    embedding = embedding[0]

                data.append({
                    "id": i,
                    "vector": embedding,
                    "text": chunk.page_content
                })

                excel_data.append({
                    "id": i,
                    "chunk": chunk.page_content,
                    "vector": str(embedding)
                })

            except Exception as e:
                print(f"Error processing chunk {i}: {str(e)}")

        print(f"Prepared {len(data)} records for insertion")

    except Exception as e:
        print("Error preparing data:", str(e))
        traceback.print_exc()
        return

    

    # =====================================
    # 7. Insert into Milvus
    # =====================================

    try:
        VectorStore.insert(
            collection_name="rag_collection",
            data=data
        )

        # VectorStore.flush(collection_name="rag_collection")

        print(f"{len(data)} documents inserted successfully")

        try:
            stats = VectorStore.get_collection_stats("rag_collection")
            print("Collection Stats:", stats)

        except Exception as e:
            print("Could not fetch collection stats:", str(e))

    except Exception as e:
        print("Error inserting documents into Milvus:", str(e))
        traceback.print_exc()
        return

    # =====================================
    # 8. Vector Search
    # =====================================

    try:
        query = "bradsol terminated me ,what are the benefits i will avail from bradsol?"

        print("\nRunning Vector Search...")

        results = vector_search(query=query, top_k=25)

        print(f"\nRetrieved {len(results)} chunks")

        for i, result in enumerate(results):
            print(f"\nChunk {i + 1}")
            print("-" * 80)
            print(result)

    except Exception as e:
        print("Error in Vector Search:", str(e))
        traceback.print_exc()


    try:
        print("Running Re-Ranking....")
        results = re_rank_documents(results, query)
        print(f"\nTop Re-ranked Chunks:")
        for i, result in enumerate(results):
            print(f"\nChunk {i + 1}")
            print("-" * 80)
            print(result)
    except Exception as e:
        print("Error in Re-Ranking:", str(e))
        traceback.print_exc()   

    try:
        print("Generating Response from LLM...")
        response = generate_response(query=query,retrieved_chunks=results)
        print("\nGenerated Response:")
        print("-" * 80)
        print(response) 
    except Exception as e:
        print("Error in Generating Response:", str(e))
        traceback.print_exc()   

    

    # =====================================
    # Final Summary
    # =====================================

    try:
        end_time = time.time()
        total_time = round(end_time - start_time, 2)

        print("\n" + "=" * 80)
        print("RAG PIPELINE COMPLETED SUCCESSFULLY")
        print("=" * 80)
        print(f"Execution Time: {total_time} seconds")
        

    except Exception as e:
        print("Error in Final Summary:", str(e))


if __name__ == "__main__":
    rag_pipeline()