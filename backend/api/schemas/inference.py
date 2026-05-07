from unittest.mock import Base

from pydantic import BaseModel


class InferenceRequest(BaseModel):
    model: str # TODO: enum model names
    prompt: str
    temperature: float | None = 0.7