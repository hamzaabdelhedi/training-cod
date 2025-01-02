
from pydantic import BaseModel, Field

class TrainerCreate(BaseModel):
    name: str = Field(..., example="Ghassen Souga")
    expertise: str = Field(..., example="Python Development")
    contact_info: str = Field(..., example="souga.ghassen-prestataire@ca-gip.fr")

class TrainerResponse(BaseModel):
    id: str = Field(..., example="63f9cd041c4b5c0a5f8c4e6d")
    name: str = Field(..., example="Ghassen Souga")
    expertise: str = Field(..., example="Python Development")
    contact_info: str = Field(..., example="souga.ghassen-prestataire@ca-gip.fr")
