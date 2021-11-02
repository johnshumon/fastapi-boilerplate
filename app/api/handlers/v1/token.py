"""
Token handler module. Access token needs to be
obtained in order to access authorized endpoints.
"""

from typing import Any
from fastapi import APIRouter

from app.schemas import CreateToken, CreateTokenResponse
from app.auth import encode_jwt

router = APIRouter()


@router.post("", response_model=CreateTokenResponse)
async def create_token(body: CreateToken) -> Any:
    """
    JWT handler.
    """

    access_token = encode_jwt(body.email)
    return {"access_token": access_token}
