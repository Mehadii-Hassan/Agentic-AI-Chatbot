from langchain_mistralai import ChatMistralAI
from langchain.tools import tool
from dotenv import load_dotenv
load_dotenv()


# custom tool
@tool
def get_text_length(text: str) -> int:
    """Returns the number of character in a given text"""
    return len(text)

# define llm
llm = ChatMistralAI(
    model = "mistral-small-2506",
    temperature = 0.7
)

# tool binding
llm_with_tool = llm.bind_tools([get_text_length])

result = llm_with_tool.invoke("hello")
print(result)