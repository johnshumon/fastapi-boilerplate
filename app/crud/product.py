""""""

import logging

from app.crud.base import CRUDBase
from app.models.product import Product
from app.schemas import CreateProduct, UpdateProduct

logger = logging.getLogger(__name__)


class CRUDProduct(CRUDBase[Product, CreateProduct, UpdateProduct]):
    # Declare model specific CRUD operation methods.
    pass


product = CRUDProduct(Product)
