from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings



def create_vector_store(all_splits):

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vector_store = Chroma(
                            collection_name="MedBook",
                            embedding_function=embeddings,
                            persist_directory="./upload",  # Where to save data locally, remove if not necessary
                                            )

    document_ids = vector_store.add_documents(documents=all_splits)

    return vector_store