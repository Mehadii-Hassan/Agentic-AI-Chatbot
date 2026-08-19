import os
from typing import TypedDict

# create the state
class pipelinestate(TypedDict):
    raw_input : str
    edited_text : str
    script_text : str
    final_output : str 


# define llm
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature = 0.7
)


# create node
# 1st node
def editor_node(state : pipelinestate) -> dict:
    """Stage 1: Cleans up grammar, removes typos and refines the tone"""

    prompt = (
        "You are an expert copyeditor. Clean up the following raw text."
        "Fix any grammatical error, spelling mistakes, and smooth out the transition flow"
        "while keeping the core message intact. Return only the edited text. \n\n"
        f"Text : \n{state['raw_input']}"
    )
    response = llm.invoke(prompt)
    return {"edited_text" : response.content.strip()}


# 2nd node
def scriptwriter_node(state : pipelinestate) -> dict:
    """Stage 2: Formats the clean text into an engaging video script style."""

    prompt = (
        "You are a charismatic YouTube contect creator. Take this edited text and transform"
        "it into a highly engaging, punchy, conversational video script hook. Make it sound"
        "like a real person speaking passionately. Return only the script content.\n\n"
        f"Edited Text: \n{state['edited_text']}"
    )
    response = llm.invoke(prompt)
    return {"script_text" : response.content.strip()}


# 3rd node
def translator_node(state : pipelinestate) -> dict:
    """Stage 3: Translate the script into natural flowing Banglish."""

    prompt = (
        "You are an expert content localizer for the Bangladeshi market. "
        "Convert the following script into natural, flowing Banglish: a comfortable mix of Bangla "
        "and English written in Bangla script where appropriate. Do not translate word for word, "
        "repeat information, or change the original meaning. Keep the tone conversational, clear, "
        "and engaging, like an intellectual tech educator speaking naturally on a live stream. "
        "Return only final Banglish text.\n\n"
        f"Script: \n{state['script_text']}"
    )
    response = llm.invoke(prompt)
    return {"final_output" : response.content.strip()}


# create graph
from langgraph.graph import StateGraph, START, END

graph = StateGraph(pipelinestate)

# add the nodes in out graph
graph.add_node("editor", editor_node)
graph.add_node("scriptwriter", scriptwriter_node)
graph.add_node("translator", translator_node)

# add edges (sequential - one after another)
graph.add_edge(START, "editor")
graph.add_edge("editor", "scriptwriter")
graph.add_edge("scriptwriter", "translator")
graph.add_edge("translator", END)

# compile the graph
app = graph.compile()

result = app.invoke({
    "raw_input" : "AI agents are the future of tech. They can think, plan and act on their own. Lnaggraph helps you build these agents with proper control and memory."
})

print(result['final_output'])