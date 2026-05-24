from libraries import *


def extension_detector(file_path):
    if file_path.endswith(".pdf"):
        return "pdf"
    elif file_path.endswith(".docx"):
        return "docx"
    elif file_path.endswith(".txt"):
        return "txt"
    elif file_path.endswith(".csv"):
        return "csv"
    elif file_path.endswith(".xlsx"):
        return "xlsx"
    


def load_document(file_path):
    file_extension = extension_detector(file_path)
    if file_extension == "pdf":
        loader = PyPDFLoader(file_path)
        document = loader.load()
    elif file_extension == "docx":
        loader = UnstructuredWordDocumentLoader(file_path)
        document = loader.load()
    elif file_extension == "txt":
        loader = TextLoader(file_path)
        document = loader.load()
    elif file_extension == "csv":
        loader = CSVLoader(file_path)
        document = loader.load()
    elif file_extension == "xlsx":
        # Handle Excel files if needed

        pass
    else:
        raise ValueError("Unsupported file type")
    
    for doc in document:

        doc.metadata.update({

            "file_name":
            os.path.basename(file_path),

            "source_path":
            file_path,

            "file_type":
            file_extension,

            "ingestion_time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "file_size_kb":
            round(
                os.path.getsize(file_path)
                / 1024, 2
            )
        })
    return document






def ingest_data(file_paths):
    documents = []
    for file_path in file_paths:
        if os.path.isfile(file_path):
            document = load_document(file_path)
            documents.extend(document)

    return documents

    