### for single page
# from langchain_community.document_loaders import WebBaseLoader

# url = "https://www.inceptionbd.com/"
# data = WebBaseLoader(url)
# docs = data.load()
# print(docs[0].page_content)



### for multiple page
from langchain_community.document_loaders import WebBaseLoader

urls = [
    "https://www.inceptionbd.com/",
    "https://www.inceptionbd.com/courses",
    "https://www.inceptionbd.com/instructors",
    "https://www.inceptionbd.com/course/Python-for-Beginners",
    "https://www.inceptionbd.com/course/The-Complete-Python-Course-in-English",
    "https://www.inceptionbd.com/course/Master-Generative-AI-in-Bangla",
    "https://www.inceptionbd.com/categories/Artificial-intelligence-AI",
]

loader = WebBaseLoader(urls)
docs = loader.load()

print(f"Total Documents: {len(docs)}")

for i, doc in enumerate(docs, 1):
    print(f"\n{'='*80}")
    print(f"Document {i}")
    print(f"Source: {doc.metadata.get('source')}")
    print(doc.page_content[:500])  