""""""

import logging

from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


def initialise(db: Session) -> None:
    # Write database initialisation queries.
    pass
