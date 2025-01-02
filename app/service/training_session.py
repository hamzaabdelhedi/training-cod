
from bson import ObjectId

def create_training_session(db, data):
    result = db.training_sessions.insert_one(data)
    session = db.training_sessions.find_one({"_id": result.inserted_id})
    session["id"] = str(session.pop("_id"))
    return session

def get_training_session(db, session_id):
    session = db.training_sessions.find_one({"_id": ObjectId(session_id)})
    if session:
        session["id"] = str(session.pop("_id"))
    return session

def update_training_session(db, session_id, data):
    result = db.training_sessions.update_one({"_id": ObjectId(session_id)}, {"$set": data})
    return result.modified_count > 0

def delete_training_session(db, session_id):
    result = db.training_sessions.delete_one({"_id": ObjectId(session_id)})
    return result.deleted_count > 0

def get_all_training_sessions(db):
    sessions = db.training_sessions.find()
    return [{"id": str(session.pop("_id")), **session} for session in sessions]
