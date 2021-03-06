"""
Product module.
"""

import logging
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db.session import db_connection

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("", response_model=List[schemas.ProductResponse])
async def read_products(
    db: Session = Depends(db_connection), skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve all products.
    """
    products = crud.product.get_multi(db, skip=skip, limit=limit)
    return products


@router.post("", response_model=schemas.ProductResponse)
async def create_product(
    *, db: Session = Depends(db_connection), product_in: schemas.CreateProduct
) -> Any:
    """
    Create new products.
    """
    product = crud.product.create(db, obj_in=product_in)
    return product


@router.put("", response_model=schemas.ProductResponse)
async def update_product(
    *, db: Session = Depends(db_connection), product_in: schemas.UpdateProduct
) -> Any:
    """
    Update existing products.
    """
    product = crud.product.get(db, model_id=product_in.id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    product = crud.product.update(db, db_obj=product, obj_in=product_in)
    return product


@router.delete("", response_model=schemas.Message)
async def delete_product(*, db: Session = Depends(db_connection), id: int) -> Any:
    """
    Delete existing product.
    """
    product = crud.product.get(db, model_id=id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The product with this ID does not exist in the system.",
        )
    crud.product.remove(db, model_id=product.id)
    return {"message": f"Product with ID = {id} deleted."}
