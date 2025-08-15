# 📚 Chat with your PDF using Free Hugging Face RAG

This Streamlit app lets you **chat with any PDF** using a **free Hugging Face Retrieval-Augmented Generation (RAG)** setup.  
It uses **LangChain**, **FAISS**, and **sentence-transformers** for document embedding & retrieval, and **FLAN-T5** for free text generation.

---

## 🚀 Features
- 📄 Upload and process **any PDF** (up to 200MB)
- 🧠 Ask natural language questions and get answers from your PDF
- 🔍 Uses **vector search (FAISS)** for efficient information retrieval
- 💬 Runs **entirely for free** with Hugging Face models

---

## 📷 Screenshots

### **Home Screen**
![Home Screen](Screenshot%20(71).png)

### **Example Interaction**
![Example Chat](Screenshot2.png)  
*(Replace `Screenshot2.png` with your actual second screenshot file name)*

---

## 📂 Project Structure
.
├── app.py # Main Streamlit app
├── utils.py # Utility functions for PDF loading, splitting, and vector store creation
├── requirements.txt # Python dependencies
├── uploaded_files/ # Stores uploaded PDFs
└── README.md # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/6303-naidu/Langchain-Chatpdf.git
cd Langchain-Chatpdf


##Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate    # On Mac/Linux
venv\Scripts\activate       # On Windows


####Install Dependencies
pip install -r requirements.txt


####Requirements

Your requirements.txt:

langchain
sentence-transformers
faiss-cpu
PyPDF2
streamlit
transformers
torch
pypdf
langchain-community


###Running the App

#Run the Streamlit app locally:

streamlit run app.py