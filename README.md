 # 🩺 DiReCT – Diagnostic Knowledge Graph & Retrieval System  

DiReCT is a **diagnostic knowledge graph and intelligent retrieval system** designed to organize, analyze, and query medical documents efficiently.  
It leverages **NLP, knowledge graph techniques, and semantic search** to provide healthcare professionals with accurate and structured diagnostic information.  

---
![image alt](https://github.com/AlishbaNazir/RAG-Clinical-Notes-Summarizer/blob/main/ChatGPT%20Image%20Aug%2031,%202025,%2001_04_01%20AM.png?raw=true)
---
## 🚀 Features  
- 📑 **Document Processing** – Handles structured & unstructured medical documents.  
- 🧠 **Knowledge Graph Generation** – Builds a graph representation of medical entities and their relationships.  
- 🔎 **Semantic Search** – Uses vector similarity (FAISS) for efficient and intelligent query retrieval.  
- 📊 **Data Analysis** – Provides insights from flattened diagnostic datasets.  
- ⚡ **Streamlit/Flask App** – User-friendly interface for running the diagnostic retrieval system.  

---

## 🛠️ Tech Stack  
- **Languages:** Python  
- **Libraries:** Pandas, NumPy, FAISS, NetworkX, PyTorch/TensorFlow, Scikit-learn  
- **Frameworks:** Flask / Streamlit  
- **Data:** Medical diagnostic documents (`finished_data.csv`, `diagnostic_kg_data_flattened.xlsx`)  

---

## 📂 Project Structure  
```
├── app.py                     # Main application file  
├── requirements.txt           # Project dependencies  
├── medical_docs_faiss.index   # Vector index for semantic search  
├── finished_data.csv          # Processed dataset  
├── diagnostic_kg_data_flattened.xlsx # Knowledge graph data  
├── notebooks/                 # Jupyter notebooks for experiments  
└── README.md                  # Project documentation  
```

---

## ⚙️ Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/DiReCT.git
   cd DiReCT-main
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Run the application:  
   ```bash
   python app.py
   ```  

---

## 📊 Example Use Cases  
- A doctor searches for a condition → system retrieves related diagnostics & treatment info.  
- A researcher queries medical terms → semantic search finds similar cases across documents.  
- Medical knowledge graph → shows entity relationships (symptom ↔ disease ↔ treatment).  

---

## 🔮 Future Improvements  
- Integration with **LLM-based medical assistants**.  
- Real-time knowledge graph visualization.  
- Support for multilingual medical documents.  

---

## 👩‍💻 Contributors  
- **Alishba Nazir**  


---

## 📬 Contact  
For queries or collaboration:  
📧 [alishbanazir910@gmail.com] | 🌐 [https://github.com/AlishbaNazir]  
