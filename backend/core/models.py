from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the story option presented to the user.")
    nextNode: Dict[str, Any] = Field(description="The next story node that this option leads to.")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="The content of the story node.")
    isEnding: bool = Field(description="Indicates if this node is an ending.")
    isWinningEnding: bool = Field(description="Indicates if this ending is a winning outcome.")
    isWinningEnding: bool = Field(description="Indicates if this ending is a winning outcome.")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description = "The list of options available at this story node.")

class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story.")
    rootNode: StoryNodeLLM = Field(description="The root node of the story.")
