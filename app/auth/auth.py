"""
Authentication module
"""

import time
from typing import Any

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
    access_token = jwt.encode(
        payload, settings.SIGNING_KEY, algorithm=settings.SIGNING_ALGORITHM
    ).decode("utf-8")

    return access_token


def decode_jwt(token: str) -> Any:
    """
    Checks if a given jwt is valid. If it is
    then request is further allowed to access
    intended API.
    """

    try:
        decoded_token = jwt.decode(
            token,
            settings.SIGNING_KEY,
            algorithms=settings.SIGNING_ALGORITHM,
            issuer=settings.TOKEN_ISSUER,
            audience=settings.TOKEN_AUDIENCE,
        )
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except Exception as err:
        logger.error(err)
        return None


def generate_token(user_email: str) -> str:
    return encode_jwt(user_email)


def is_valid_token(token: str) -> bool:
    return True if decode_jwt(token) else False
