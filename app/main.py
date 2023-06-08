from fastapi import Body, FastAPI, Request

from app import db, fuzzy, models

app = FastAPI()


@app.on_event("startup")
def on_startup():
    app.mongo_client, app.database, app.collection = db.connect()


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongo_client.close()


@app.get("/")
def home():
    pass


@app.get("/fuzzy")
def get_fuzzy_url(request: Request):
    return fuzzy.list_fuzzy_url(request=request)


@app.post("/fuzzy")
def make_fuzzy_url(request: Request, data: models.URL = Body(...)):
    return fuzzy.generate_fuzzy_url(request=request, data=data)


@app.post("/mail")
def mail_user():
    pass


@app.get("{uid}")
def open_fuzzy_url(uid: str):
    pass
