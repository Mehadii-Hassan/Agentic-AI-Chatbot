from dotenv import load_dotenv

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 3,
        "fetch_k": 10,
        "lambda_mult": 0.5
    }
)

llm = ChatMistralAI(
    model="mistral-small-2506"
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful AI assistant.

Use ONLY the provided context.

If the answer is not in the context say:

I could not find the answer in the document.
"""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}
"""
    )
])

print("RAG Ready")

while True:

    query = input("\nYou: ")

    if query.lower() in ["0", "exit", "quit"]:
        break

    retrieved_docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    final_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(final_prompt)

    print("\nAI:", response.content)