"""
Message module template
"""

import logging

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class Message(BaseModel):
    message: str
