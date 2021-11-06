"""
User module. This module contains handlers related
to user signup, login, and update details.
"""

from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth import generate_token
from app.crud.user import user
from app.db.session import db_connection
from app.schemas import CreateUser, CreateUserResponse

router = APIRouter()


@router.post("", response_model=CreateUserResponse)
async def create_user(userdata: CreateUser, db: Session = Depends(db_connection)) -> Any:
    """
    User signup handler
    Takes user details, and uses user-email to create a
    JWT as a access token.
    """

    try:
        user.create(userdata, db)
        access_token = generate_token(userdata.email)

        return {
            "status": True,
            "message": "Successfully created the user!",
            "access_token": access_token,
        }
    except Exception as err:
        # TODO: replace print with logger
        print("-----------------------------")
        print("Error: ", err)
        print("-----------------------------")

        return {
            "status": False,
            "message": "Could not create the user.",
            "access_token": "",
        }
