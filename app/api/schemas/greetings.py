from enum import Enum

from pydantic import BaseModel, Field


class Tone(str, Enum):
    """
    Enum for the possible tones of the greeting.
    """

    FRIENDLY = "friendly"
    ANGRY = "angry"
    NEUTRAL = "neutral"


class GreetingRequest(BaseModel):
    """
    Defines the expected input data structure.
    """

    username: str = Field(
        default="world",
        description="The name of the user to greet.",
        examples=["Alice"],
    )
    tone: Tone = Field(
        default=Tone.NEUTRAL,
        description="The tone of the greeting.",
        examples=["friendly"],
    )


class GreetingResponse(BaseModel):
    """
    Defines the output data structure.
    """

    greeting: str = Field(
        description="The generated greeting message.",
        examples=["Hello, world."],
    )
