# This file is responsible for signing, encoding, decoding, and returning JWTs.

import time

import jwt

from app import config

settings = config.get_settings()

JWT_SECRET = settings.auth_secret
JWT_ALGORITHM = settings.auth_algorithm


def token_response(token: str):
    # Function returns generated tokens(JWTs)
    return {
        "access_token": token
    }


def signJWT(userID: str):
    # Function used for signing the JWT string
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decodeJWT(token: str):
    # Function used for decoding the JWT string
    try:
        decode_token = jwt.decode(
            token, key=JWT_SECRET, algorithms=JWT_ALGORITHM)
        return decode_token if decode_token['expiry'] >= time.time() else None
    except Exception:
        return {}
