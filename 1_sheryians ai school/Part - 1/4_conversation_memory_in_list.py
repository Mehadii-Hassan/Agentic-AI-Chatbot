from dotenv import load_dotenv
load_dotenv()

### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )

# create a list for conversation memory
messages = []

print("---welcome! write 'exit' for exit the app---")
while True: 
    prompt = input("You: ")
    messages.append(prompt) #prompt append in messags list

    if prompt == "exit":
        break

    response = model.invoke(messages)
    messages.append(response.content) #response append in messags list
    print("Bot: ", response.content)

print(messages)