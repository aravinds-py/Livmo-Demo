# 🩺 Healthcare RAG + Multi-Agent AI Assistant

A production-style Healthcare Retrieval-Augmented Generation (RAG) system built using FastAPI, semantic search, hybrid retrieval, vector embeddings, MLflow tracking, and a Streamlit frontend.

This project demonstrates how modern AI systems can answer healthcare-related questions using grounded knowledge retrieval instead of relying purely on LLM memory.

---

# 🚀 Features

✅ Healthcare-focused Retrieval-Augmented Generation (RAG)  
✅ Hybrid Retrieval (Dense + Sparse Search)  
✅ Semantic Search using SentenceTransformers  
✅ BM25 Sparse Retrieval  
✅ Vector Embedding Pipeline  
✅ Document Chunking & Indexing  
✅ FastAPI Backend APIs  
✅ Streamlit Interactive UI  
✅ MLflow Experiment Tracking  
✅ Safety-aware Healthcare Routing  
✅ Modular AI System Architecture  

---

# 🧠 System Architecture

```text
User Question
      │
      ▼
Streamlit Frontend
      │
      ▼
FastAPI Backend API
      │
      ▼
Healthcare Agent Workflow
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Safety   Retrieval Pipeline
Check        │
             ▼
      Hybrid Retrieval
     ┌───────────────┐
     │ Dense Search  │
     │ BM25 Search   │
     └───────────────┘
             │
             ▼
       Relevant Chunks
             │
             ▼
      Grounded Response
             │
             ▼
        MLflow Logging
```

---

# 📂 Project Structure

```text
Livmo-Demo/
│
├── app/
│   ├── api/
│   │   └── routes.py
│   │
│   ├── agents/
│   │   └── workflow.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── llm.py
│   │
│   ├── retrieval/
│   │   ├── chunking.py
│   │   ├── indexer.py
│   │   └── retriever.py
│   │
│   ├── evaluation/
│   │   └── tracking.py
│   │
│   └── main.py
│
├── data/
│   ├── healthcare_docs/
│   └── index.json
│
├── frontend/
│   └── app.py
│
├── scripts/
│   └── ingest.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | FastAPI |
| Frontend | Streamlit |
| Embeddings | SentenceTransformers |
| Retrieval | Hybrid Dense + BM25 |
| Vector Search | NumPy Similarity |
| Experiment Tracking | MLflow |
| Language | Python |
| API Testing | Swagger UI |
| AI Concepts | RAG, Semantic Search, Vector Embeddings |

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/healthcare-rag-agent.git

cd healthcare-rag-agent
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create `.env`

```env
OPENAI_API_KEY=

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

MLFLOW_TRACKING_URI=./mlruns
```

---

# 📚 Add Healthcare Knowledge Base

Add `.txt` healthcare files inside:

```text
data/healthcare_docs/
```

Example:
- diabetes.txt
- hypertension.txt
- discharge_guidelines.txt

---

# 🧱 Build Vector Index

```bash
python -m scripts.ingest
```

This step:
- loads healthcare documents
- chunks text
- generates embeddings
- creates vector index

---

# 🚀 Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Open Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# 💻 Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

Open:

```text
http://localhost:8501
```

---

# 🧪 Example Questions

```text
What lifestyle habits help manage high blood pressure?
```

```text
Why is medication adherence important for diabetes?
```

```text
What should I do if I have chest pain?
```

---

# 📊 MLflow Tracking

Start MLflow UI:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

Tracked metrics:
- latency
- retrieved sources
- route type
- question logs
- answer logs

---

# 🔍 Retrieval Pipeline

## Dense Retrieval
Uses:
- SentenceTransformers
- semantic similarity
- embedding vectors

## Sparse Retrieval
Uses:
- BM25 keyword retrieval

## Hybrid Retrieval
Combines:
- semantic search
- keyword search
for better retrieval quality.

---

# 🛡️ Safety Layer

The system includes a healthcare safety routing mechanism.

Urgent keywords such as:
- chest pain
- stroke
- difficulty breathing

trigger emergency guidance responses instead of normal retrieval.

---

# 🎯 Learning Outcomes

This project helped me understand:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- Hybrid retrieval systems
- FastAPI backend engineering
- MLflow experiment tracking
- AI system architecture
- Healthcare-focused AI workflows
- Modular AI application design

---

# 🚧 Future Improvements

- HyDE Query Expansion
- Cross-Encoder Reranking
- LangGraph Multi-Agent Routing
- Pinecone/ChromaDB Integration
- Docker Deployment
- GCP/AWS Deployment
- Authentication Layer
- Conversational Memory
- Streaming Responses

---

# 📸 Demo Screenshots

## Streamlit UI

_Add screenshot here_

---

## Swagger API Docs

_Add screenshot here_

---

## MLflow Dashboard

_Add screenshot here_

---

# ⚠️ Disclaimer

This project is for educational and portfolio purposes only.

It does not provide:
- medical diagnosis
- treatment recommendations
- professional healthcare advice

Always consult licensed healthcare professionals for medical concerns.

---

# 👨‍💻 Author

## Aravind Seenivasan

AI Engineer | RAG Systems | LLM Applications | FastAPI | NLP | Generative AI

📧 aravindsmy@yahoo.com  
🔗 LinkedIn: https://linkedin.com/in/aravindssr  
💻 GitHub: https://github.com/aravinds-py

---

# ⭐ If you found this useful

Give this repository a star ⭐
