from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

data = PyPDFLoader("data\\deeplearning.pdf")
docs = data.load()

#chunking
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 10,
)
chunks = splitter.split_documents(docs)  #chunking


### embedding model
embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

# vector store (chroma)
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="chroma-db"
)

# similarity search
results = vectorstore.similarity_search(
    "what is used for data analysis?",
    k=2,
)

for r in results:
    print(r.page_content)
    print(r.metadata)

# retriever
retriever = vectorstore.as_retriever()

docs = retriever.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)