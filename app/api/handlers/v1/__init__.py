from fastapi import APIRouter

from app.api.handlers.v1 import home, product, token, user

api_router = APIRouter()

api_router.include_router(home.router, prefix="/home", tags=["general"])

# product endpoint examples. currently commented out.
# api_router.include_router(product.router, prefix="/products", tags=["products"])

# auth and user endpoints
api_router.include_router(token.router, prefix="/tokens", tags=["auths"])
api_router.include_router(user.router, prefix="/users/signup", tags=["users"])
