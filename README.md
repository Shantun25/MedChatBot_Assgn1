# 🩺 MedBot: AI-Powered Medical Chatbot

**MedBot** is a Retrieval-Augmented Generation (RAG)–based AI assistant designed to answer medical questions using a reference medical knowledge base. It uses state-of-the-art language models, embedding techniques, and vector storage to deliver accurate and context-aware responses on topics like symptoms, medications, diagnostics, treatments, and preventive healthcare.

---


## 🧱 Project Structure


      App/
            ├── main.py                  # FastAPI app
            ├── document_loader.py       # PDF parsing and chunking
            ├── vector_store.py          # Chroma for embedding and 
            ├── qa_chain.py              # LangGraph QA pipeline
      templates/
            ├──index.html
      static/
            ├──style.css
      requirements.txt         # Not Included (Need to Install dependencies)
      .env                     # Not Included (Requires Google API Key)
      README.md                

## 📄 requirements.txt

    fastapi
    uvicorn
    langchain
    langchain-community pymupdf
    langgraph
    langchain-text-splitters
    langchain-chroma
    langchain-google-genai
    python-multipart

## ⚙️ Setup Instructions

### 1. Clone the Repository

### 2. Create a `.env` File

Create a `.env` file in the root directory with the following contents:

```env
GOOGLE_API_KEY="your API Key"
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```



## 🚀 Running the App

    uvicorn main:app --reload

  Then visit: http://127.0.0.1:8000/docs to test the API.

## ✅ Features
- Upload a PDF research paper
- Automatically extract, chunk, and embed using Google Gemini
- Ask questions via /ask/ endpoint
- Uses LangChain for retrieval and generation
  


## ⚠️ Disclaimer

This project is intended for educational purposes only and does **not** constitute professional medical advice. Always consult a licensed medical practitioner for diagnosis or treatment.

---

## 🙌 Author

**SB**  
*MedBot: Your AI Health Companion*
