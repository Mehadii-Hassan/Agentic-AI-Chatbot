from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

data = TextLoader("data\\notes.txt")
docs = data.load()

#chunking
splitter = CharacterTextSplitter(
    chunk_size = 10,
    chunk_overlap = 1,
    separator = ""   #iccha/oicchik
)
chunk = splitter.split_documents(docs)  #chunking

print(len(chunk))