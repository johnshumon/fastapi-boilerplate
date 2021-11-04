"""Product schema module"""

from typing import Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    price: Optional[float]


class CreateProduct(ProductBase):
    name: str
    price: float


class UpdateProduct(ProductBase):
    id: int
    pass


class ProductResponse(ProductBase):
    class Config:
        orm_mode = True
