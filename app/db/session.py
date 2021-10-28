""""""

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import settings

logger = logging.getLogger(__name__)
engine = create_engine(settings.DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
