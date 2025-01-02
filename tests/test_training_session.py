
import pytest
from unittest.mock import MagicMock

from bson import ObjectId

from app.service.training_session import (
    create_training_session,
    get_training_session,
    update_training_session,
    delete_training_session,
    get_all_training_sessions,
)

@pytest.fixture
def setup():
    db = MagicMock()
    mock_id = str(ObjectId())
    return db, mock_id

def test_create_training_session(setup):
    db, mock_id = setup
    session_data = {
        "training_id": "mock_training_id",
        "date": "2025-01-01",
        "location": "Online",
        "trainer": "mock_trainer_id",
        "trainees": ["mock_trainee_id"],
    }
    db.training_sessions.insert_one.return_value.inserted_id = mock_id
    db.training_sessions.find_one.return_value = {**session_data, "_id": ObjectId(mock_id)}
    session = create_training_session(db, session_data)
    assert session["id"] == mock_id

def test_get_training_session(setup):
    db, mock_id = setup
    session_data = {
        "training_id": "mock_training_id",
        "date": "2025-01-01",
        "location": "Online",
        "trainer": "mock_trainer_id",
        "trainees": ["mock_trainee_id"],
    }
    db.training_sessions.find_one.return_value = {**session_data, "_id": ObjectId(mock_id)}
    session = get_training_session(db, mock_id)
    assert session["id"] == mock_id

def test_update_training_session(setup):
    db, mock_id = setup
    db.training_sessions.update_one.return_value.modified_count = 1
    success = update_training_session(db, mock_id, {"location": "Updated Location"})
    assert success is True

def test_delete_training_session(setup):
    db, mock_id = setup
    db.training_sessions.delete_one.return_value.deleted_count = 1
    success = delete_training_session(db, mock_id)
    assert success is True

def test_get_all_training_sessions(setup):
    db, mock_id = setup
    db.training_sessions.find.return_value = [
        {
            "_id": ObjectId(mock_id),
            "training_id": "mock_training_id",
            "date": "2025-01-01",
            "location": "Online",
            "trainer": "mock_trainer_id",
            "trainees": ["mock_trainee_id"],
        }
    ]
    sessions = get_all_training_sessions(db)
    assert len(sessions) == 1
    assert sessions[0]["id"] == mock_id
