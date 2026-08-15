from dotenv import load_dotenv
load_dotenv()


### for openai
# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(
#     model = "gpt-5",
#     temperature=0.7
#     )
# response = model.invoke("what is cricket?")
# print(response.content)


# ## for gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flast",
#     temperature=0.7
#     )
# response = model.invoke("what is cricket?")
# print(response.content)


# ## for groq
# from langchain_groq import ChatGroq
# model = ChatGroq(
#     model = "openai/gpt-oss-120b",
#     temperature=0.7
#     )
# response = model.invoke("what is cricket?")
# print(response.content)


### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )
response = model.invoke("what is cricket?")
print(response.content)