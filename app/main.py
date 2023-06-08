from fastapi import FastAPI

from app import db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    app.mongo_client, app.database, app.collection = db.connect()


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongo_client.close()


@app.get("/")
def start_new_page():
    return {
        "HOST": str(app.mongo_client),
        "DB": str(app.database),
        "COLLECTION": str(app.collection)
    }
