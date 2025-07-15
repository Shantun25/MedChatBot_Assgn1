from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text_from_pdf(tmp_path):

    print('tmp_path ',tmp_path)
    loader = PyMuPDFLoader(
            #file_path = "Medical_book.pdf",
            file_path = tmp_path,
            # headers = None
            # password = None,
            mode = "single")

    docs = []
    docs_lazy = loader.load_and_split()

    for doc in docs_lazy:
        docs.append(doc)

    return docs


def chunk_text(docs):

    text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1000,  # chunk size (characters)
                    chunk_overlap=200,  # chunk overlap (characters)
                    add_start_index=True,  # track index in original document
                    )

    all_splits = text_splitter.split_documents(docs)

    return all_splits
