"""
User schema module
"""

from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    password: Optional[str]


class CreateUser(UserBase):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Abu",
                "lastname": "Shumon",
                "email": "email@shumon.me",
                "password": "nopassword",
            }
        }


class CreateUserResponse(BaseModel):
    status: bool
    message: str
    access_token: str

    class Config:
        schema_extra = {
            "example": {
                "status": True,
                "message": "Successfully created the user!",
                "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                ".eyJpcMdcpiJsb2NhbGhvc3QiLCJpYXQiOjE2MzYwMTUwNzgsImV4cCI6MTYzNjAxNjg3OCwiYXVkIjoiZW1haWxAc2h1bW9uLm1lIn0.0slVFU_INXv13X4yQAvW1VCNJI6XUu5qOP6aPXD03VM",
            }
        }
