"""Authentication module"""

import time

import jwt

from app.core import settings


def encode_jwt(user_email: str) -> str:
    """Generates JWT"""

    # The JWT specification defines some registered claim names
    # and how they should be used. Following terms describe
    # what they stand for.
    # > iss: Issuer Claim
    # > iat: Issued At Claim
    # > exp: Expiration Time Claim
    # > aud: Audience Claim
    # Token is valid for 30 minutes. It can be set to shorter/longer
    # time depending on need.
    # ===========================

    payload = {
        "iss": settings.TOKEN_ISSUER,
        "iat": int(time.time()),
        "exp": int(time.time() + float(settings.VALIDATION_PERIOD)),
        "aud": user_email,
    }
    access_token = jwt.encode(payload, settings.SIGNING_KEY, algorithm=settings.SIGNING_ALGORITHM).decode("utf-8")

    return access_token


def get_token():
    pass
