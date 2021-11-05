"""Database connection module"""

from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import settings

engine = create_engine(settings.DB_URL, pool_pre_ping=True)


def initialise() -> bool:
    """
    Database connection initializer.
    """
    try:
        if engine.connect():
            return True

    except Exception as err:
        print("-----------------------------")
        print("Err: ", err)
        print("-----------------------------")
        raise err


def db_connection() -> Generator:
    """
    Database connection generator.
    Returns a generator object if engine connects successfully.
    """
    try:
        if initialise():
            db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
            yield db
    finally:
        db.close()
