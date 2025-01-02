
import pytest
from unittest.mock import MagicMock

from bson import ObjectId

from app.service.trainee import create_trainee, get_trainee, update_trainee, delete_trainee, get_all_trainees

@pytest.fixture
def setup():
    db = MagicMock()
    mock_id = str(ObjectId())
    return db, mock_id

def test_create_trainee(setup):
    db, mock_id = setup
    trainee_data = {"name": "Jane Doe", "contact_info": "jane.doe@example.com"}
    db.trainees.insert_one.return_value.inserted_id = mock_id
    db.trainees.find_one.return_value = {**trainee_data, "_id": ObjectId(mock_id)}
    trainee = create_trainee(db, trainee_data)
    assert trainee["id"] == mock_id

def test_get_trainee(setup):
    db, mock_id = setup
    trainee_data = {"name": "Jane Doe", "contact_info": "jane.doe@example.com"}
    db.trainees.find_one.return_value = {**trainee_data, "_id": ObjectId(mock_id)}
    trainee = get_trainee(db, mock_id)
    assert trainee["id"] == mock_id

def test_update_trainee(setup):
    db, mock_id = setup
    db.trainees.update_one.return_value.modified_count = 1
    success = update_trainee(db, mock_id, {"name": "Updated Name"})
    assert success is True

def test_delete_trainee(setup):
    db, mock_id = setup
    db.trainees.delete_one.return_value.deleted_count = 1
    success = delete_trainee(db, mock_id)
    assert success is True

def test_get_all_trainees(setup):
    db, mock_id = setup
    db.trainees.find.return_value = [
        {"_id": ObjectId(mock_id), "name": "Jane Doe", "contact_info": "jane.doe@example.com"}
    ]
    trainees = get_all_trainees(db)
    assert len(trainees) == 1
    assert trainees[0]["id"] == mock_id
