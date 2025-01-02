
from pydantic import BaseModel, Field

class TraineeCreate(BaseModel):
    name: str = Field(..., example="Jane Doe")
    contact_info: str = Field(..., example="jane.doe@ca-gip.fr")

class TraineeResponse(BaseModel):
    id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e7f")
    name: str = Field(..., example="Jane Doe")
    contact_info: str = Field(..., example="jane.doe@ca-gip.fr")
