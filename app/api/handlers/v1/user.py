"""
User module. This contains handlers related
to user signup, login, and update details.
"""

import logging

from typing import Any
from fastapi import APIRouter

from app.schemas import CreateUser, CreateUserResponse
from app.auth import generate_token

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("", response_model=CreateUserResponse)
async def create_token(body: CreateUser) -> Any:
    """
    Handler for user signup
    Takes user details, and uses user-email to create a
    JWT as a access token.
    """

    try:
        access_token = generate_token(body.email)
        return {
            "status": True,
            "message": "Successfully created the user!",
            "access_token": access_token,
        }
    except Exception as err:
        logger.error(err)

        return {
            "status": False,
            "message": "Could not create the user.",
            "access_token": "",
        }
