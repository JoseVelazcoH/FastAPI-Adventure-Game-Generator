from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class StoryOptionLLM(BaseModel):
    text: str = Field(description="The text of the option choice presented to the user")
    nextNode: Dict[str, Any] = Field(description="The complete next story node object with content, isEnding, isWinningEnding, and options fields")


class StoryNodeLLM(BaseModel):
    content: str = Field(description="The narrative content text for this story node")
    isEnding: bool = Field(description="True if this node ends the story, False otherwise")
    isWinningEnding: bool = Field(description="True if this is a winning ending, False for losing endings or non-ending nodes")
    options: Optional[List[StoryOptionLLM]] = Field(default=None, description="Array of option objects. Must be null for ending nodes, required for non-ending nodes")


class StoryLLMResponse(BaseModel):
    title: str = Field(description="The title of the story")
    rootNode: StoryNodeLLM = Field(description="The root node of the story")
