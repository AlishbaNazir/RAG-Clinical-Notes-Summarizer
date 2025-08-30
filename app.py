import streamlit as st
import os
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

st.set_page_config(page_title="Clinical RAG with MIMIC", layout="wide")
st.title("🧠 Diagnostic Reasoning RAG for Clinical Notes")

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

@st.cache_resource
def load_data_and_index():
    data_path = "mimic_docs.pkl"
    index_path = "faiss_index.bin"

    if not os.path.exists(data_path):
        st.error("Document file 'mimic_docs.pkl' not found.")
        st.stop()

    with open(data_path, "rb") as f:
        documents = pickle.load(f)

    embedder = load_embedding_model()

    if os.path.exists(index_path):
        index = faiss.read_index(index_path)
    else:
        st.info("Building FAISS index. This may take a minute...")
        doc_embeddings = embedder.encode(documents, show_progress_bar=True)
        dimension = doc_embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(doc_embeddings).astype("float32"))
        faiss.write_index(index, index_path)

    return documents, index, embedder

@st.cache_resource
def load_generator():
    model_name = "mistralai/Mistral-7B-Instruct-v0.1"
    return pipeline("text-generation", model=model_name, device_map="auto")

def retrieve_documents(query, embedder, index, documents, top_k=3):
    query_embedding = embedder.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), top_k)
    return [documents[i] for i in I[0]]

def format_prompt(query, docs):
    context = "\n\n".join(docs)
    return f"""You are a clinical assistant. Use the following clinical notes to answer the question.

### Clinical Notes:
{context}

### Query:
{query}

### Answer:"""

def generate_answer(query, docs, generator):
    prompt = format_prompt(query, docs)
    response = generator(prompt, max_new_tokens=200, temperature=0.7, do_sample=True)
    return response[0]['generated_text'].split("### Answer:")[-1].strip()

documents, index, embedder = load_data_and_index()
generator = load_generator()

query = st.text_input("Enter your clinical question:", placeholder="e.g., What are the key findings in the latest radiology note?")
top_k = st.slider("Top-K Documents to Retrieve", 1, 10, 3)

if st.button("Generate Answer"):
    with st.spinner("Retrieving relevant clinical notes..."):
        retrieved_docs = retrieve_documents(query, embedder, index, documents, top_k)

    with st.spinner("Generating response..."):
        answer = generate_answer(query, retrieved_docs, generator)

    st.subheader("📄 Retrieved Documents")
    for i, doc in enumerate(retrieved_docs):
        st.markdown(f"**Document {i+1}:**\n{doc}")
        st.markdown("---")

    st.subheader("🧠 Generated Answer")
    st.markdown(answer)
