import os
import streamlit as st
from utils import load_and_split_pdf, create_vector_store
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from transformers import pipeline

st.set_page_config(page_title="🧠 Chat with PDF (FREE RAG)", layout="wide")
st.title("📚 Chat with your PDF using Free Hugging Face RAG")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        file_path = os.path.join("uploaded_files", uploaded_file.name)
        os.makedirs("uploaded_files", exist_ok=True)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        chunks = load_and_split_pdf(file_path)
        vectordb = create_vector_store(chunks)
        retriever = vectordb.as_retriever()

        # Load free Hugging Face model
        hf_pipeline = pipeline("text2text-generation", model="google/flan-t5-base", max_length=256)
        llm = HuggingFacePipeline(pipeline=hf_pipeline)

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=retriever,
            return_source_documents=False
        )

        st.success("Ready! Ask your questions below:")
        user_query = st.text_input("Ask a question:")

        if user_query:
            with st.spinner("Generating answer..."):
                result = qa_chain.run(user_query)
                st.write("🧠 **Answer:**")
                st.write(result)
