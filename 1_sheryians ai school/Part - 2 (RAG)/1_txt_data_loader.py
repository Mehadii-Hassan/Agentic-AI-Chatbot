## txt file load
from langchain_community.document_loaders import TextLoader
data = TextLoader("data\\notes.txt")
docs = data.load()
print(docs[0].page_content)