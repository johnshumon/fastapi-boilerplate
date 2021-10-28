from fastapi import APIRouter

from app.api.handlers.v1 import home, products

api_router = APIRouter()

api_router.include_router(home.router, prefix="/home", tags=["general"])
api_router.include_router(products.router, prefix="/products", tags=["products"])
