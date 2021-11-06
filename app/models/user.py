"""
User models module
"""

from sqlalchemy import Column, Integer, String

from app.models import Base


class User(Base):
    """User class"""

    id: int = Column(Integer, primary_key=True, index=True)
    firstname: str = Column(String(50), nullable=False)
    lastname: str = Column(String(50), nullable=False)
    email: str = Column(String(100), nullable=False)
    password: str = Column(String(100), nullable=False)
    # username: str = Column(String(50), nullable=False)
