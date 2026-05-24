
# 🚀 Advanced Retrieval-Augmented Generation System

A production-grade **End-to-End Retrieval-Augmented Generation (RAG) Pipeline** built using **LangChain, NVIDIA Embeddings, Milvus Vector Database, Azure OpenAI, and Re-Ranking techniques** for intelligent enterprise document retrieval and grounded response generation.

---

## 📌 Features

✅ **Document Ingestion**  
Supports loading multiple document formats for enterprise knowledge retrieval.

✅ **Document Chunking**  
Recursive chunking strategy for optimized semantic retrieval.

✅ **Embeddings Generation**  
NVIDIA embedding models for high-quality semantic vector representation.

✅ **Vector Database**  
Milvus-powered vector storage and similarity search.

✅ **Retrieval Mechanisms**
- Semantic Vector Search
- Full Text Search
- Hybrid Search

✅ **Re-Ranking**
Improves retrieval relevance using NVIDIA Re-Ranker.

✅ **Context Building**
Optimized context construction for grounded LLM responses.

✅ **LLM Response Generation**
Azure OpenAI integration for accurate and context-aware answers.

✅ **Unit Testing**
Comprehensive test coverage for ingestion, chunking, embeddings, vector DB, and LLM components.

---

## 🏗️ Architecture

```text
User Query
    ↓
Query Embedding
    ↓
Milvus Vector Search
    ↓
Re-Ranking
    ↓
Context Building
    ↓
Prompt Engineering
    ↓
Azure OpenAI (LLM)
    ↓
Grounded Response
````

---

## 📂 Project Structure

```text
End_to_End_Rag
├── A(or)B_Testing
├── Chunking
│   └── Document_Chunker.py
├── Context_Building
├── Data_Ingestion
│   ├── Data_Monitor.py
│   └── Document_Loader.py
├── Embeddings
│   └── Generate_Embeddings.py
├── LLM
│   └── Generate_Response.py
├── Monitoring_Evaluation
├── Reranking
│   └── re_ranker.py
├── Similarity_Retrieval
│   ├── Full_Text_Search.py
│   ├── Hybrid_Search.py
│   └── Vector_Search.py
├── User Query
├── Vector_Database
│   └── Milvus_Vector_DB.py
├── orchestrator
│   └── rag_pipeline.py
├── unit_testing
├── libraries.py
├── main.py
├── requirements.txt
└── pyproject.toml
```

---

## ⚙️ Tech Stack

* **Python**
* **LangChain**
* **Azure OpenAI**
* **NVIDIA Embeddings**
* **Milvus Vector Database**
* **Reranking**
* **Hybrid Search**
* **PyTest**
* **LangChain Documents**
* **Semantic Search**

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/radhirsh/Advanced-Retrieval-Augmented-Generation-System.git
```

Move to project folder:

```bash
cd Advanced-Retrieval-Augmented-Generation-System
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_DEPLOYMENT=
AZURE_OPENAI_KEY=

NVIDIA_EMBEDDINGS_KEY=
NVIDIA_EMBEDDING_MODEL=

MILVUS_DB_PATH=
```

---

## ▶️ Run the Pipeline

```bash
python main.py
```

or

```bash
python orchestrator/rag_pipeline.py
```

---

## 🧪 Run Unit Tests

```bash
pytest unit_testing/
```

---

## 📈 Future Enhancements

* Agentic RAG
* Multi-Agent Retrieval
* Knowledge Graph Integration
* Hallucination Detection
* Langfuse Observability
* Context Compression
* Hybrid Ranking Optimization
* A/B Testing for Retrieval Quality

---

## 👨‍💻 Author

**Sridhar S**
AI/ML Engineer | Generative AI | Agentic AI | RAG Systems

---

## 📜 License

This project is licensed under the MIT License.



