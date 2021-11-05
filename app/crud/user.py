"""Create user database module"""

from typing import Dict

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.user import CreateUser


class UserOperations(BaseModel):
    """
    User class for database related operations.
    """
    @staticmethod
    def create(user_data: CreateUser):
        print("coming here")
        session = Session()
        # serialized_data = jsonable_encoder(user_data)
        print("worked until here")
        # db_obj = UserModel(**serialized_data)
        session.add(user_data)
        session.commit()
        # session.refresh(db_obj)

        return db_obj

    # def create(self, db: Session, *, obj_in: CreateSchemaType) -> ModelType:
    #     obj_in_data = jsonable_encoder(obj_in)
    #     db_obj = self.model(**obj_in_data)
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj
