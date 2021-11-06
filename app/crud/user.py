"""
User CRUD module.
Provides functionality to read, create, update, and delete
functionalities of the user model
"""

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import CreateUser


class CRUDUser(BaseModel):
    """
    class for user's CRUD operations.
    """
    def create(self, userdata: CreateUser, db: Session):
        serialized_data = jsonable_encoder(userdata)
        db_obj = User(**serialized_data)
        db.add(db_obj)
        db.commit()

        return db_obj


user = CRUDUser()
