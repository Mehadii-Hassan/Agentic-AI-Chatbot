from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
import os
from langgraph.graph.message import add_messages

load_dotenv()

#initial model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=os.environ.get("GEMINI_API_KEY")
)

# Define states
class Chatstate(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: Chatstate):
    messages = state["messages"] #take user query from state
    response = llm.invoke(messages) #send to llm
    return {"messages": [response]} #return the response in the state

#Connection with database
conn = sqlite3.connect(database="chatbot.db", check_same_thread=False)
checkpoint = SqliteSaver(conn) #save the state of the chatbot to memory

#Create graph
graph = StateGraph(Chatstate)
#add nodes
graph.add_node("chat_node", chat_node)
#add edges
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)
#compile graph
chatbot = graph.compile(checkpointer=checkpoint)


# CONFIG = {"configurable": {"thread_id": "default_thread:1"}}
# res = chatbot.invoke(
#     {"messages": [HumanMessage(content="My name is mainul")]},
#     config=CONFIG
# )
# print(res)


def get_all_threads():
    all_threads = set()
    for ckpt in checkpoint.list(None):
        all_threads.add(ckpt.config["configurable"]["thread_id"])

    return (list(all_threads))
