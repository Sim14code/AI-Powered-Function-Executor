# AI-Powered-Function-Executor
# 📌 AI-Powered Function Executor

## 🚀 Overview
AI-Powered Function Executor is a Python-based API service that leverages **LLM + RAG (Retrieval-Augmented Generation)** to dynamically retrieve and execute automation functions based on user prompts. The system processes user inputs, maps them to predefined functions, and generates executable Python code for invocation.

## 🎯 Features
✅ **Function Registry** – Predefined automation functions (e.g., open applications, system monitoring, command execution)
✅ **RAG-Based Function Retrieval** – Stores function metadata in a vector database and retrieves the best match
✅ **Dynamic Code Generation** – Generates structured Python scripts for function execution
✅ **Context-Aware Execution** – Uses session-based memory for better function retrieval
✅ **FastAPI-Based API Service** – Exposes a REST API for function execution
✅ **Extensible & Scalable** – Can support user-defined functions in the future

## 🛠 Tech Stack
- **Python** (Core language)
- **FastAPI** (API framework)
- **FAISS** (Vector database for retrieval)
- **Sentence-Transformers** (LLM embeddings)
- **Uvicorn** (ASGI server)
- **Psutil** (System control & automation)


## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Sim14code/AI-Powered-Function-Executor.git
cd AI-Powered-Function-Executor
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Running the API
Start the FastAPI server using Uvicorn:
```bash
uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

## 🔥 Usage
### API Endpoint
**POST /execute**
#### Request:
```json
{
  "prompt": "Open calculator"
}
```
#### Response:
```json
{
  "function": "open_calculator",
  "code": "<Generated Code Snippet>"
}
```

## 📌 Future Enhancements
- ✅ Logging & monitoring for function execution
- ✅ Support for custom user-defined functions
- ✅ Multi-user session handling


