from fastapi import Body, FastAPI, Request, Response

from app import db, fuzzy, mail_service, models

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


@app.get("/fuzzy", response_model=models.ListDocument)
def get_fuzzy_url(request: Request):
    return fuzzy.list_fuzzy_url(request=request)


@app.post("/fuzzy")
def make_fuzzy_url(request: Request, response: Response,
                   data: models.URL = Body(...)):
    return fuzzy.generate_fuzzy_url(
        request=request,
        data=data,
        response=response
    )


@app.post("/mail")
async def mail_user(request: Request, response: Response,
                    email_data: models.EmailSchema):
    ret_val = await mail_service.send_mail(
        request=request,
        email_data=email_data,
        response=response
    )
    return ret_val


@app.get("{uid}")
def open_fuzzy_url(uid: str):
    pass
