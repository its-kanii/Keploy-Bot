# 🤖 Keploy RAG Bot (LLaMA3 + Groq + FAISS)

A Retrieval-Augmented Generation (RAG) based chatbot powered by **LLaMA3** on **Groq**, built to answer questions about **Keploy** and API Testing tools. It uses **FAISS** for vector storage and **HuggingFace embeddings** to encode documents. The system supports both CLI and Gradio-based user interfaces.

---

## 📁 Project Structure

```

keploy-rag-bot/
│
├── data/                        # Data and documents to be ingested
│   └── keploy\_docs/
│       └── keploy\_resources.json
│
├── keploy\_vectordb/            # Stored FAISS vector index
│
├── scripts/
│   ├── ingest\_docs.py          # Script to convert documents to embeddings and store in FAISS
│   ├── query\_vector\_db.py      # Low-level script to query FAISS DB
│   └── rag\_generate.py         # RAG pipeline (retrieval + LLM generation)
│
├── app/
│   └── gradio\_ui.py            # Gradio UI for chat interface
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Setup Instructions

### 1. Clone and Install Dependencies
```bash
git clone https://github.com/its-kanii/keploy-rag-bot.git
cd keploy-rag-bot
pip install -r requirements.txt
````

### 2. Set Environment Variables

You’ll need the following keys:

* **GROQ\_API\_KEY** (for accessing LLaMA3)
* (Optional) **HUGGINGFACEHUB\_API\_TOKEN** if you use HuggingFaceHub models

Set them in your environment or `.env` file:

```bash
export GROQ_API_KEY=your_key_here
export HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## 📚 Prepare the Vector Store

Run the ingestion script to create `keploy_vectordb` from your JSON documents:

```bash
python scripts/ingest_docs.py
```

---

## 💬 Run Chatbot

### CLI Mode:

```bash
python scripts/rag_generate.py
```

### Gradio UI:

```bash
python app/gradio_ui.py
```

Then open the link displayed in your terminal (usually `http://127.0.0.1:7860`).

---

## 🧠 How It Works

1. **Ingestion**: JSON documents are read and embedded using `sentence-transformers/all-MiniLM-L6-v2`.
2. **Vector Store**: Embeddings are stored in a FAISS index (`keploy_vectordb/`).
3. **RAG Flow**:

   * User query is embedded.
   * Top-k matching docs are retrieved using FAISS.
   * The context is combined with the query and passed to LLaMA3 via Groq API.

---

## 🔗 Sample Sources Used

* [Keploy Docs](https://docs.keploy.io/)
* [Postman API Testing](https://www.postman.com/api-testing)
* [Mocking & Stubbing APIs](https://www.mockable.io/docs/mock-api)

---

## 🚀 Future Improvements

* Add feedback/rating system for responses
* Support more LLM backends (OpenAI, Anthropic, etc.)
* Deploy on cloud (Hugging Face Spaces / Vercel)

---

## 🛠️ Tech Stack

* 🧠 LLM: LLaMA3 via Groq API
* 🧠 Embeddings: HuggingFace (MiniLM-L6-v2)
* 📦 Vector DB: FAISS
* 🔌 LangChain (RAG orchestration)
* 🖥️ UI: Gradio / CLI / (optionally Flask)

---

## 👩‍💻 Maintainer

**Kanimozhi K**
📬 [LinkedIn](https://www.linkedin.com/in/kanimozhi-kathirvel)
📧 [Gmail](mailto:kanimeena678@gmail.com)

---

## ⭐ Star This Repo

If this helped you, consider starring ⭐ the repo and sharing feedback!

