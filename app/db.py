import pymongo
from dotenv import load_dotenv

from app import config

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
