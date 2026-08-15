from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )


# prompt template
prompt = ChatPromptTemplate.from_messages([
   ("system",
"""
You are a professional Movie Information Extraction Assistant.

Your task:
Extract useful structured information from a movie paragraph and present it 

Rules:
- Do not add explanations
- Do not add extra commentary
- Follow the exact format
- If information is missing than write NULL
- Keep summary short (2-3 lines max)
- Do not guess unknown facts

Output Format:

Movie Title:
Release Year:
Genre:
Director:
Main Cast:
Setting/Location:
Plot:
Themes:
Ratings:
Notable Features:

Short Summary:
"""),

("human",
"""
Extract information from this paragraph: {paragraph}
""")
]
)


para = input("Give your paragraph: ")
final_prompt = prompt.invoke({"paragraph" : para})


response = model.invoke(final_prompt)
print(response.content)