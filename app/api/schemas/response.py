from pydantic import BaseModel


class InferenceResponse(BaseModel):
    provider: str
    response: str
    cached: bool = False