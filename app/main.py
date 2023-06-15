from fastapi import Body, Depends, FastAPI, Request, Response

from app import db, fuzzy, mail_service, models, user_util
from app.auth import jwt_bearer

app = FastAPI()


@app.on_event("startup")
def on_startup():

    app.mongo_client, app.database = db.connect()


@app.on_event("shutdown")
def shutdown_db_client():

    app.mongo_client.close()


@app.get("/fuzzy", response_model=models.ListDocument,
         dependencies=[Depends(jwt_bearer.jwtBearer())],
         summary="List URLs")
def get_fuzzy_url(request: Request):

    return fuzzy.list_fuzzy_url(request=request)


@app.post("/fuzzy",
          dependencies=[Depends(jwt_bearer.jwtBearer())],
          summary="Generate Fuzzy URLs")
def make_fuzzy_url(request: Request, response: Response,
                   data: models.URL = Body(...)):
    return fuzzy.generate_fuzzy_url(
        request=request,
        data=data,
        response=response
    )


@app.post("/mail",
          dependencies=[Depends(jwt_bearer.jwtBearer())],
          summary="Mail User")
async def mail_user(request: Request, response: Response,
                    email_data: models.EmailSchema = Body(...)):

    ret_val = await mail_service.send_mail(
        request=request,
        email_data=email_data,
        response=response
    )
    return ret_val


@app.get("/{uid}", summary="Redirect URL")
def open_fuzzy_url(request: Request, uid: str):

    return fuzzy.redirect_fuzzy_url(request=request, uid=uid)


@app.post('/user/signup', tags=["user"])
def user_signup(
        request: Request,
        user: models.UserSchema = Body(default=None)):

    return user_util.signup(request=request, data=user)


@app.post('/user/login', tags=["user"])
def user_login(
        request: Request,
        user: models.UserLoginSchema = Body(default=None)):

    return user_util.login(request=request, data=user)
