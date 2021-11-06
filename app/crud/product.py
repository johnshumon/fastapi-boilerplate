"""
Product CRUD module.
Provides CRUD functionalities of the product model.
"""

from app.crud.base import CRUDBase
from app.models.product import Product
from app.schemas import CreateProduct, UpdateProduct


class CRUDProduct(CRUDBase[Product, CreateProduct, UpdateProduct]):
    # Declare model specific CRUD operation methods.
    pass


product = CRUDProduct(Product)
