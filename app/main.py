from fastapi import FastAPI

from app import db

app = FastAPI()


@app.on_event("startup")
def on_startup():
    db.connect()


@app.get("/")
def start_new_page():
    return {"HELLO": "WORLD"}
