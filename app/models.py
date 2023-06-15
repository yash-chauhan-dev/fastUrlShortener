import uuid
from typing import List

from pydantic import AnyHttpUrl, BaseModel, EmailStr, Field


class DatabaseDocument(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    original_url: AnyHttpUrl = Field(...)
    fuzzy_url: AnyHttpUrl = Field(...)


class OriginalUrl(BaseModel):
    original_url: AnyHttpUrl = Field(...)


class URL(BaseModel):
    url: AnyHttpUrl = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "url": "http://www.test.com/"
            }
        }


class ListDocument(BaseModel):
    message: str = Field(...)
    data: List[dict] = Field(...)


class EmailSchema(BaseModel):
    email: List[EmailStr]


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Ronald",
                "email": "ronald@test.com",
                "password": "123"
            }
        }


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "email": "ronald@test.com",
                "password": "123"
            }
        }
