"""Token schema module"""

from typing import Optional

from pydantic import BaseModel, Field, EmailStr


class CreateToken(BaseModel):
    firstname: str = Field(...)
    lastname: str = Field(...)
    email: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "firstname": "Abu",
                "lastname": "Shumon",
                "email": "email@shumon.me"
            }
        }


class CreateTokenResponse(BaseModel):
    access_token: str
