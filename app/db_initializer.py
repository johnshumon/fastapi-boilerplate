import logging

from typing import Optional

from alembic import command
from alembic.config import Config

from app.db.initialise import initialise
from app.db.session import SessionLocal

logger = logging.getLogger(__name__)


def run_migrations(script_location: str, db_url: Optional[str]) -> None:
    """Runs  migrations"""
    logger.info(f"Running DB migrations in {script_location}")
    alembic_cfg = Config()
    alembic_cfg.set_main_option("script_location", script_location)
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)
    command.upgrade(alembic_cfg, "head")


if __name__ == "__main__":
    # TODO: Run migration before spinning up the server.
    # But for now keep migration off.
    # run_migrations("./app/migrations", DB_URL)

    db = SessionLocal()
    initialise(db)
