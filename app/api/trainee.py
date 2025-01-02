
from fastapi import APIRouter, Depends, HTTPException
from app.models.trainee import TraineeCreate, TraineeResponse
from app.service.trainee import create_trainee, get_trainee, update_trainee, delete_trainee, get_all_trainees
from app.database.db import get_db

router = APIRouter()

@router.post("/", response_model=TraineeResponse)
def create_trainee_endpoint(trainee: TraineeCreate, db=Depends(get_db)):
    return create_trainee(db, trainee.dict())

@router.get("/{trainee_id}", response_model=TraineeResponse)
def get_trainee_endpoint(trainee_id: str, db=Depends(get_db)):
    trainee = get_trainee(db, trainee_id)
    if not trainee:
        raise HTTPException(status_code=404, detail="Trainee not found")
    return trainee

@router.put("/{trainee_id}")
def update_trainee_endpoint(trainee_id: str, trainee: TraineeCreate, db=Depends(get_db)):
    success = update_trainee(db, trainee_id, trainee.dict())
    if not success:
        raise HTTPException(status_code=404, detail="Update failed")
    return {"message": "Trainee updated successfully"}

@router.delete("/{trainee_id}")
def delete_trainee_endpoint(trainee_id: str, db=Depends(get_db)):
    success = delete_trainee(db, trainee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Trainee not found")
    return {"message": "Trainee deleted successfully"}

@router.get("/", response_model=list[TraineeResponse])
def get_all_trainees_endpoint(db=Depends(get_db)):
    return get_all_trainees(db)
