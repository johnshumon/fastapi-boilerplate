from fastapi import APIRouter

from app.api.handlers.v1 import home, product, token

api_router = APIRouter()

api_router.include_router(home.router, prefix="/home", tags=["general"])

api_router.include_router(product.router, prefix="/products", tags=["products"])

# auth and user endpoints
api_router.include_router(token.router, prefix="/tokens", tags=["auth"])
