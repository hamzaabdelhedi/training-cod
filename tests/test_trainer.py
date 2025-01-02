
import pytest
from unittest.mock import MagicMock
from bson import ObjectId
from app.service.trainer import create_trainer, get_trainer, update_trainer, delete_trainer, get_all_trainers

@pytest.fixture
def setup():
    db = MagicMock()
    mock_id = str(ObjectId())
    return db, mock_id

def test_create_trainer(setup):
    db, mock_id = setup
    trainer_data = {"name": "John Doe", "expertise": "Python", "contact_info": "john@example.com"}
    db.trainers.insert_one.return_value.inserted_id = mock_id
    db.trainers.find_one.return_value = {**trainer_data, "_id": ObjectId(mock_id)}
    trainer = create_trainer(db, trainer_data)
    assert trainer["id"] == mock_id

def test_get_trainer(setup):
    db, mock_id = setup
    trainer_data = {"name": "John Doe", "expertise": "Python", "contact_info": "john@example.com"}
    db.trainers.find_one.return_value = {**trainer_data, "_id": ObjectId(mock_id)}
    trainer = get_trainer(db, mock_id)
    assert trainer["id"] == mock_id

def test_update_trainer(setup):
    db, mock_id = setup
    db.trainers.update_one.return_value.modified_count = 1
    success = update_trainer(db, mock_id, {"name": "Updated Name"})
    assert success is True

def test_delete_trainer(setup):
    db, mock_id = setup
    db.trainers.delete_one.return_value.deleted_count = 1
    success = delete_trainer(db, mock_id)
    assert success is True

def test_get_all_trainers(setup):
    db, mock_id = setup
    db.trainers.find.return_value = [
        {"_id": ObjectId(mock_id), "name": "John Doe", "expertise": "Python", "contact_info": "john@example.com"}
    ]
    trainers = get_all_trainers(db)
    assert len(trainers) == 1
    assert trainers[0]["id"] == mock_id
