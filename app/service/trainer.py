
from bson import ObjectId

def create_trainer(db, data):
    result = db.trainers.insert_one(data)
    trainer = db.trainers.find_one({"_id": result.inserted_id})
    trainer["id"] = str(trainer.pop("_id"))
    return trainer

def get_trainer(db, trainer_id):
    trainer = db.trainers.find_one({"_id": ObjectId(trainer_id)})
    if trainer:
        trainer["id"] = str(trainer.pop("_id"))
    return trainer

def update_trainer(db, trainer_id, data):
    result = db.trainers.update_one({"_id": ObjectId(trainer_id)}, {"$set": data})
    return result.modified_count > 0

def delete_trainer(db, trainer_id):
    result = db.trainers.delete_one({"_id": ObjectId(trainer_id)})
    return result.deleted_count > 0

def get_all_trainers(db):
    trainers = db.trainers.find()
    return [{"id": str(trainer.pop("_id")), **trainer} for trainer in trainers]
