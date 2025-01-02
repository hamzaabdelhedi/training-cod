
from bson import ObjectId

def create_trainee(db, data):
    result = db.trainees.insert_one(data)
    trainee = db.trainees.find_one({"_id": result.inserted_id})
    trainee["id"] = str(trainee.pop("_id"))
    return trainee

def get_trainee(db, trainee_id):
    trainee = db.trainees.find_one({"_id": ObjectId(trainee_id)})
    if trainee:
        trainee["id"] = str(trainee.pop("_id"))
    return trainee

def update_trainee(db, trainee_id, data):
    result = db.trainees.update_one({"_id": ObjectId(trainee_id)}, {"$set": data})
    return result.modified_count > 0

def delete_trainee(db, trainee_id):
    result = db.trainees.delete_one({"_id": ObjectId(trainee_id)})
    return result.deleted_count > 0

def get_all_trainees(db):
    trainees = db.trainees.find()
    return [{"id": str(trainee.pop("_id")), **trainee} for trainee in trainees]
