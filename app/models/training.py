
from pydantic import BaseModel, Field

class TrainingCreate(BaseModel):
    title: str = Field(..., example="Kubernetes and Cloud Native Tools V1")
    description: str = Field(..., example="An introductory on CA-GIP Cloud Native tools.")

class TrainingResponse(BaseModel):
    id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e8f")
    title: str = Field(..., example="Kubernetes and Cloud Native Tools V1")
    description: str = Field(..., example="An introductory on CA-GIP Cloud Native tools.")
