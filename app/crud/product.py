""""""

import logging

from app.crud.base import CRUDBase
from app.models.product import Product
from app.schemas import ProductCreate, ProductUpdate

logger = logging.getLogger(__name__)


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    # Declare model specific CRUD operation methods.
    pass


product = CRUDProduct(Product)
