
import os
from pymongo import MongoClient

def get_db():
    host = os.getenv("MONGO_HOST", "mongodb://localhost:27017")
    database_name = os.getenv("MONGO_DATABASE", "training_cod")
    username = os.getenv("MONGO_USERNAME", "cod")
    password = os.getenv("MONGO_PWD", "cod_pwd")
    client = MongoClient(host, username=username, password=password)
    return client[database_name]

def get_client():
    host = os.getenv("MONGO_HOST", "mongodb://localhost:27017")
    database_name = os.getenv("MONGO_DATABASE", "training_cod")
    username = os.getenv("MONGO_USERNAME", "cod")
    password = os.getenv("MONGO_PWD", "cod_pwd")
    client = MongoClient(host, username=username, password=password)
    return client
