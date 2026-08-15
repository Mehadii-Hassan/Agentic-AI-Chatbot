from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()


### load the data for txt file
data = TextLoader("data\\notes.txt")
docs = data.load()

### prompt template
template = ChatPromptTemplate.from_messages(
    [("system", "you are a AI that summarizes the text"),
     ("human", "{data}")]
)

### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )

### prompt
prompt = template.format_messages(data = docs[0].page_content)

response = model.invoke(prompt)
print(response.content)

print(docs[0].page_content)