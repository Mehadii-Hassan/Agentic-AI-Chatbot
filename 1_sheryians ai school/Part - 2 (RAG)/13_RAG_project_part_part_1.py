from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv

load_dotenv()

print("Loading PDF...")
loader = PyPDFLoader("data/deeplearning.pdf")
docs = loader.load()


print("Splitting...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)
print(f"Chunks: {len(chunks)}")


embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


print("Creating Vector Database...")
Chroma.from_documents(
    documents=chunks,
    embedding=embedding,
    persist_directory="chroma_db"
)

print("Done!")