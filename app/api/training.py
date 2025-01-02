
from fastapi import APIRouter, Depends, HTTPException
from app.models.training import TrainingCreate, TrainingResponse
from app.service.training import create_training, get_training, update_training, delete_training, get_all_trainings
from app.database.db import get_db

router = APIRouter()

@router.post("/", response_model=TrainingResponse)
def create_training_endpoint(training: TrainingCreate, db=Depends(get_db)):
    return create_training(db, training.dict())

@router.get("/{training_id}", response_model=TrainingResponse)
def get_training_endpoint(training_id: str, db=Depends(get_db)):
    training = get_training(db, training_id)
    if not training:
        raise HTTPException(status_code=404, detail="Training not found")
    return training

@router.put("/{training_id}")
def update_training_endpoint(training_id: str, training: TrainingCreate, db=Depends(get_db)):
    success = update_training(db, training_id, training.dict())
    if not success:
        raise HTTPException(status_code=404, detail="Update failed")
    return {"message": "Training updated successfully"}

@router.delete("/{training_id}")
def delete_training_endpoint(training_id: str, db=Depends(get_db)):
    success = delete_training(db, training_id)
    if not success:
        raise HTTPException(status_code=404, detail="Training not found")
    return {"message": "Training deleted successfully"}

@router.get("/", response_model=list[TrainingResponse])
def get_all_trainings_endpoint(db=Depends(get_db)):
    return get_all_trainings(db)
