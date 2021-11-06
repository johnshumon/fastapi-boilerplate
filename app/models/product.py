"""
Product models module
"""

from sqlalchemy import Column, Float, Integer, String

from app.models import Base


class Product(Base):
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=False)
    price: float = Column(Float, nullable=False)
