# for creating any graph firstly we need to create state

import os

# 1. typed Dictionary (most common approach)
from typing import TypedDict

class State(TypedDict):
    topic : str
    summary : str
    score : int


# 2. Pydantic approach (good for data validation & type checking runtime)
from pydantic import BaseModel, field_validator

class State(BaseModel):
    topic : str
    summary : str 
    score : int

    @field_validator
    def score_positive(cls, value):
        if value < 0:
            raise ValueError("Score must be positive")


# 3. Python data classes (used very rarely)
from dataclasses import dataclass, field

@dataclass
class State:
    topic : str = ""
    summary : str = ""
    messages : list = field(default_factory=list)


# 4. using langgraph
from langgraph.graph import MessagesState

class State(MessagesState):
    user_name : str
    language : str 