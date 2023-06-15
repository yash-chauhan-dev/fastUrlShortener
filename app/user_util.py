from fastapi import Request

from app import db, models
from app.auth import jwt_handler


def signup(request: Request, data: models.UserSchema):
    ret_val = db.add_user(request=request, user_data=data)
    if ret_val:
        jwt_token = jwt_handler.signJWT(data.email)
        return jwt_token
    else:
        return {"error": "Error signing new user"}


def login(request: Request, data: models.UserLoginSchema):
    if check_user(request=request, data=data):
        jwt_token = jwt_handler.signJWT(data.email)
        return jwt_token
    else:
        return {"error": "Invalid login details!"}


def check_user(request: Request, data: models.UserLoginSchema):
    ret_val = db.get_user(request=request, user_data=data)
    return True if ret_val else False
