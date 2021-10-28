""""""

import logging

from typing import Generator

from app.db.session import SessionLocal

logger = logging.getLogger(__name__)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
