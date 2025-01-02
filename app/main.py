
from fastapi import FastAPI
from app.api.trainer import router as trainer_router
from app.api.trainee import router as trainee_router
from app.api.training import router as training_router
from app.api.training_session import router as training_session_router
from app.database.db import get_db, get_client
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.mongodb_client = get_db()
    app.mongodb_client.command("ping")
    print("MongoDB connection established")

@app.on_event("shutdown")
async def shutdown():
    app.mongodb_client = get_client()
    app.mongodb_client.close()
    print("MongoDB connection closed")

app.include_router(trainer_router, prefix="/trainers", tags=["Trainers"])
app.include_router(trainee_router, prefix="/trainees", tags=["Trainees"])
app.include_router(training_router, prefix="/training", tags=["Training"])
app.include_router(training_session_router, prefix="/training_session", tags=["Training Session"])

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)