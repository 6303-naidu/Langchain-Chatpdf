## 🧠 RAG Chatbot for PDFs (Free & Local)

This is a fully **free** Retrieval-Augmented Generation (RAG) chatbot that allows you to **chat with your own PDFs** using:

- 💬 **LangChain**
- 🧠 **Hugging Face Embeddings & LLM**
- 🧾 **FAISS** (vector database)
- 📚 **Streamlit UI**

---

## 🚀 Features

- ✅ 100% Free (no OpenAI API needed)
- ✅ Uses `sentence-transformers` for embeddings
- ✅ Uses `flan-t5-base` Hugging Face model
- ✅ Local FAISS vector store
- ✅ Upload and chat with any PDF
- ✅ Clean Streamlit UI

---

## 🧰 Tech Stack

| Component | Tool |
|----------|------|
| UI | Streamlit |
| Embeddings | `all-MiniLM-L6-v2` |
| LLM | `flan-t5-base` |
| Vector DB | FAISS |
| PDF Loader | LangChain + PyPDF2 |

---

## 📦 Installation

```bash
git https://github.com/6303-naidu/Langchain-Chatpdf.git
cd rag-pdf-chatbot
pip install -r requirements.txt
streamlit run app.py
