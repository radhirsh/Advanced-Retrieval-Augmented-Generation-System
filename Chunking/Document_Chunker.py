from libraries import *

text_splitter=RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50,separators=["\n\n","\n"," ", ""]
)




def chunk_documents(all_documents):
    chunked_documents=text_splitter.split_documents(all_documents)
    for i ,chunk in enumerate(chunked_documents):
        chunk.metadata['chunk_id']=i
        chunk.metadata[
            "chunking_time"
        ] = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    return chunked_documents