from dotenv import load_dotenv
load_dotenv()

# for openai
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model = "text-embedding-3-large",
    dimenstion=64
)

texts = [
    "hello this is mehadi",
    "hello your name is youtube",
    "and you are beautiful"
]

vector = embeddings.embed_documents(texts)
print(vector)