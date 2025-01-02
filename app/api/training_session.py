
from fastapi import APIRouter, Depends, HTTPException
from app.models.training_session import TrainingSessionCreate, TrainingSessionResponse
from app.service.training_session import (
    create_training_session,
    get_training_session,
    update_training_session,
    delete_training_session,
    get_all_training_sessions,
)
from app.database.db import get_db

router = APIRouter()

@router.post("/", response_model=TrainingSessionResponse)
def create_training_session_endpoint(session: TrainingSessionCreate, db=Depends(get_db)):
    return create_training_session(db, session.dict())

@router.get("/{session_id}", response_model=TrainingSessionResponse)
def get_training_session_endpoint(session_id: str, db=Depends(get_db)):
    session = get_training_session(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Training session not found")
    return session

@router.put("/{session_id}")
def update_training_session_endpoint(session_id: str, session: TrainingSessionCreate, db=Depends(get_db)):
    success = update_training_session(db, session_id, session.dict())
    if not success:
        raise HTTPException(status_code=404, detail="Update failed")
    return {"message": "Training session updated successfully"}

@router.delete("/{session_id}")
def delete_training_session_endpoint(session_id: str, db=Depends(get_db)):
    success = delete_training_session(db, session_id)
    if not success:
        raise HTTPException(status_code=404, detail="Training session not found")
    return {"message": "Training session deleted successfully"}

@router.get("/", response_model=list[TrainingSessionResponse])
def get_all_training_sessions_endpoint(db=Depends(get_db)):
    return get_all_training_sessions(db)
