### pdf file load
from langchain_community.document_loaders import PyPDFLoader
data = PyPDFLoader("data\\GRU.pdf")
docs = data.load()
print(docs)