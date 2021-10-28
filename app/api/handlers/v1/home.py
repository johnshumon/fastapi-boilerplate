"""Home handler module"""

import logging

from typing import Any
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("")
async def read_root() -> Any:
    """Main handler for the root path"""
    return {"message": "Hello FastAPI!"}
