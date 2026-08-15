from langchain_core import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv
load_dotenv()


### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )

# create a list for conversation memory
messages = [
    SystemMessage(content = "You are a funny AI agent")  #SystemMessage
]

print("---welcome! write 'exit' for exit the app---")
while True: 
    prompt = input("You: ")
    messages.append(HumanMessage(content = prompt)) #HumanMessage

    if prompt == "exit":
        break

    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content)) #AIMessage
    print("Bot: ", response.content)

print(messages)