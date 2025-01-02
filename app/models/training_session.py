
from pydantic import BaseModel, Field
from typing import List

class TrainingSessionCreate(BaseModel):
    training_id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e8f")
    date: str = Field(..., example="2025-01-01")
    location: str = Field(..., example="Online")
    trainer: str = Field(..., example="63f9cd041c4b5c0a5f8c4e6d")
    trainees: List[str] = Field(..., example=["63f9cd041c4b5c0a5f8c4e7f"])

class TrainingSessionResponse(BaseModel):
    id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e9f")
    training_id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e8f")
    date: str = Field(..., example="2025-01-01")
    location: str = Field(..., example="Online")
    trainer: str = Field(..., example="63f9cd041c4b5c0a5f8c4e6d")
    trainees: List[str] = Field(..., example=["63f9cd041c4b5c0a5f8c4e7f"])
