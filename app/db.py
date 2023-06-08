import pymongo
from dotenv import load_dotenv
from fastapi import Request
from fastapi.encoders import jsonable_encoder

from app import config, models

settings = config.get_settings()

load_dotenv()
MONGO_DB_HOST = settings.db_host
DB_STR = settings.db_str
DB_COLLECTION_STR = settings.db_collection_str


def connect():
    client = pymongo.MongoClient(host=MONGO_DB_HOST)
    db = client[DB_STR]
    collection = db[DB_COLLECTION_STR]
    return client, db, collection


def save_document(request: Request, data):
    try:
        validated_data = jsonable_encoder(models.DatabaseDocument(**data))

    except Exception:
        validated_data = None
    if validated_data is not None:
        request.app.collection.insert_one(validated_data)
        return {"message": "success"}
    else:
        return {"message": "failure"}


def list_documents(request: Request):
    return list(request.app.collection.find())
