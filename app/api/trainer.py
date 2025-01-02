
from fastapi import APIRouter, Depends, HTTPException
from app.models.trainer import TrainerCreate, TrainerResponse
from app.service.trainer import create_trainer, get_trainer, update_trainer, delete_trainer, get_all_trainers
from app.database.db import get_db

router = APIRouter()

@router.post("/", response_model=TrainerResponse)
def create_trainer_endpoint(trainer: TrainerCreate, db=Depends(get_db)):
    return create_trainer(db, trainer.dict())

@router.get("/{trainer_id}", response_model=TrainerResponse)
def get_trainer_endpoint(trainer_id: str, db=Depends(get_db)):
    trainer = get_trainer(db, trainer_id)
    if not trainer:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return trainer

@router.put("/{trainer_id}")
def update_trainer_endpoint(trainer_id: str, trainer: TrainerCreate, db=Depends(get_db)):
    success = update_trainer(db, trainer_id, trainer.dict())
    if not success:
        raise HTTPException(status_code=404, detail="Update failed")
    return {"message": "Trainer updated successfully"}

@router.delete("/{trainer_id}")
def delete_trainer_endpoint(trainer_id: str, db=Depends(get_db)):
    success = delete_trainer(db, trainer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Trainer not found")
    return {"message": "Trainer deleted successfully"}

@router.get("/", response_model=list[TrainerResponse])
def get_all_trainers_endpoint(db=Depends(get_db)):
    return get_all_trainers(db)
