"""Application entry point: Main app"""

from app.core.config import settings
from app.server import init_server
from app.services import init_db, run_migrations

if __name__ == "__main__":
    # Usually migration is run at the beginning
    # before starting up the server. But for now
    # keep migration off.
    run_migrations(settings.MIGRATION_SCRIPT_LOCATION, settings.DB_URL)

    # Initialize db and start the server.
    init_db()
    init_server()
