from langchain_community.document_loaders import (
    PyPDFLoader,
    PyMuPDFLoader,
    UnstructuredWordDocumentLoader,
    CSVLoader,
    TextLoader
)
from langchain_core.documents import Document



from dotenv import load_dotenv

import os
from datetime import datetime

documents_path=os.getenv("document_folder_path")



import os
import json
from datetime import datetime, timedelta


from langchain_classic.text_splitter import RecursiveCharacterTextSplitter

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings


load_dotenv()


import os
import traceback

# from langchain_milvus import Milvus
from pymilvus import MilvusClient



