import pymongo
# from dotenv import load_dotenv
from fastapi import Request
from fastapi.encoders import jsonable_encoder

from app import config, models

settings = config.get_settings()

# load_dotenv()
MONGO_DB_HOST = settings.db_host
DB_STR = settings.db_str
USER_COLLECTION = settings.user_collection
URL_COLLECTION = settings.url_collection


def connect():
    client = pymongo.MongoClient(host=MONGO_DB_HOST)
    db = client[DB_STR]
    return client, db


def save_document(request: Request, data):
    try:
        validated_data = jsonable_encoder(models.DatabaseDocument(**data))

    except Exception:
        validated_data = None
    if validated_data is not None:
        request.app.database[URL_COLLECTION].insert_one(validated_data)
        return {"message": "success"}
    else:
        return {"message": "failure"}


def list_documents(request: Request):
    return list(request.app.database[URL_COLLECTION].find())


def get_original_url(request: Request, url):
    ret_val = request.app.database[URL_COLLECTION].find_one(
        {"fuzzy_url": url})
    validated_data = models.OriginalUrl(**ret_val)
    return validated_data


def add_user(request: Request, user_data):
    try:
        validated_data = jsonable_encoder(models.UserSchema(**user_data))
    except Exception:
        validated_data = None

    if validated_data is not None:
        request.app.database[USER_COLLECTION].insert_one(validated_data)
        return True
    else:
        return False


def get_user(request: Request, user_data):
    try:
        validated_data = jsonable_encoder(models.UserLoginSchema(**user_data))
    except Exception:
        validated_data = None

    if validated_data is not None:
        search_user = request.app.database[USER_COLLECTION].find_one(
            {"email": validated_data.email})
        return True if search_user else False
    else:
        return False
