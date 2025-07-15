from fastapi import FastAPI, Request, File, UploadFile, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os, tempfile

import getpass
from dotenv import load_dotenv

class AskRequest(BaseModel):
    question: str


# Load environment variables
load_dotenv()

# Check for Google API Key
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY environment variable not set. Please create a .env file and add it.")

from App.document_loader import extract_text_from_pdf, chunk_text
from App.vector_store import create_vector_store
from App.qa_chain import build_qa_chain


#question = '''Can you summarize the document for me'''
'''
global qa_chain

text = extract_text_from_pdf('C:\\Users\\Shantun Bhatnagar\\OneDrive\\Desktop\\CV_Shruti.pdf')
chunks = chunk_text(text)
vectorstore = create_vector_store(chunks)
qa_chain = build_qa_chain(vectorstore)

print('A.... ',question)
    
result = qa_chain.invoke({"question": question})
print('b.... ',result)

answer = result["answer"]
print('c.... ',answer)

'''


app = FastAPI()
app.mount("/static", StaticFiles(directory="App/static"), name="static")
templates = Jinja2Templates(directory="App/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload/")
async def upload_pdf(request: Request, file: UploadFile = File(...)):
    global vectorstore, qa_chain
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    text = extract_text_from_pdf(tmp_path)
    chunks = chunk_text(text)
    vectorstore = create_vector_store(chunks)
    qa_chain = build_qa_chain(vectorstore)
    os.remove(tmp_path)

    return {"success": True, "message": f"Successfully uploaded and processed {file.filename}"}


@app.post("/ask/")
async def ask_question(request: AskRequest):

    question = request.question
    
    result = qa_chain.invoke({"question": question})
    answer = result["answer"]
 
    return {"answer": answer}


