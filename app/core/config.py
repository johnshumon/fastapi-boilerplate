"""Application core configuration"""

import logging

from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    """
    This class provides core config/settins
    """

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Fast API service"
    DB_URL: str
    SIGNING_KEY: str
    SIGNING_ALGORITHM: str
    VALIDATION_PERIOD: str
    TOKEN_ISSUER: str
    TOKEN_AUDIENCE: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
