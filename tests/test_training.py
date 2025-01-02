
import pytest
from unittest.mock import MagicMock

from bson import ObjectId

from app.service.training import create_training, get_training, update_training, delete_training, get_all_trainings
@pytest.fixture
def setup():
    db = MagicMock()
    mock_id = str(ObjectId())
    return db, mock_id

def test_create_training(setup):
    db, mock_id = setup
    training_data = {"title": "Python Basics", "description": "An introductory course on Python."}
    db.trainings.insert_one.return_value.inserted_id = mock_id
    db.trainings.find_one.return_value = {**training_data, "_id": ObjectId(mock_id)}
    training = create_training(db, training_data)
    assert training["id"] == mock_id

def test_get_training(setup):
    db, mock_id = setup
    training_data = {"title": "Python Basics", "description": "An introductory course on Python."}
    db.trainings.find_one.return_value = {**training_data, "_id": ObjectId(mock_id)}
    training = get_training(db, mock_id)
    assert training["id"] == mock_id

def test_update_training(setup):
    db, mock_id = setup
    db.trainings.update_one.return_value.modified_count = 1
    success = update_training(db, mock_id, {"title": "Advanced Python"})
    assert success is True

def test_delete_training(setup):
    db, mock_id = setup
    db.trainings.delete_one.return_value.deleted_count = 1
    success = delete_training(db, mock_id)
    assert success is True

def test_get_all_trainings(setup):
    db, mock_id = setup
    db.trainings.find.return_value = [
        {"_id": ObjectId(mock_id), "title": "Python Basics", "description": "An introductory course on Python."}
    ]
    trainings = get_all_trainings(db)
    assert len(trainings) == 1
    assert trainings[0]["id"] == mock_id
