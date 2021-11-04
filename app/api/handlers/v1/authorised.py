"""
User module. This contains handlers related
to user signup, login, and update details.
"""

from typing import Any
from fastapi import APIRouter

from app.schemas import CreateUser, CreateUserResponse
from app.auth import generate_token

router = APIRouter()


@router.post("", response_model=CreateUserResponse)
async def create_token(body: CreateUser) -> Any:
    """
    Handler for user signup
    Takes user details, and uses user-email to create a
    JWT as a access token.
    """

    access_token = generate_token(body.email)
    return {"access_token": access_token}
