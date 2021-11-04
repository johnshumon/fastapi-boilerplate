"""
Token handler module. Access token needs to be
obtained in order to access authorized endpoints.
"""

from typing import Any
from fastapi import APIRouter

from app.schemas import CreateToken, CreateTokenResponse
from app.auth import generate_token

router = APIRouter()


@router.post("", response_model=CreateTokenResponse)
async def create_token(body: CreateToken) -> Any:
    """
    JWT handler.
    Takes user details and uses user-email to create a
    JWT as a access token.
    """

    access_token = generate_token(body.email)
    return {"access_token": access_token}
