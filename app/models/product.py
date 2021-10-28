from sqlalchemy import Column, Integer, String, Float

from app.models import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
