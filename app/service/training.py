
from bson import ObjectId

def create_training(db, data):
    result = db.trainings.insert_one(data)
    training = db.trainings.find_one({"_id": result.inserted_id})
    training["id"] = str(training.pop("_id"))
    return training

def get_training(db, training_id):
    training = db.trainings.find_one({"_id": ObjectId(training_id)})
    if training:
        training["id"] = str(training.pop("_id"))
    return training

def update_training(db, training_id, data):
    result = db.trainings.update_one({"_id": ObjectId(training_id)}, {"$set": data})
    return result.modified_count > 0

def delete_training(db, training_id):
    result = db.trainings.delete_one({"_id": ObjectId(training_id)})
    return result.deleted_count > 0

def get_all_trainings(db):
    trainings = db.trainings.find()
    return [{"id": str(training.pop("_id")), **training} for training in trainings]
