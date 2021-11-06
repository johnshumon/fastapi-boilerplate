"""
Dummy authorised module. Only authorised requests can
access this endpoint.
"""

from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def get_contents() -> Any:
    """
    Dummy authorised endpoint
    """

    return {"You have successfully authorised!"}
