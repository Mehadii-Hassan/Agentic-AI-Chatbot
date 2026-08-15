from dotenv import load_dotenv
load_dotenv()

### for mistral
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(
    model = "mistral-small-2506",
    temperature=0.7
    )

print("---welcome! write 'exit' for exit the app---")
while True: 
    prompt = input("You: ")
    if prompt == "exit":
        break
    response = model.invoke(prompt)
    print("Bot: ", response.content)