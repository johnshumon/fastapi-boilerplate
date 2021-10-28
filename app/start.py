"""Application entry point: Main app"""

import logging

from app.server import init_server

logger = logging.getLogger(__name__)


def _init_logging():
    level = "INFO"
    log_format = (
        "%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)s ::__%(message)s"
    )
    date_format = "%H:%M:%S"

    logging.basicConfig(level=level, format=log_format, datefmt=date_format)


def main() -> None:
    _init_logging()

    # spin up the server
    init_server()


if __name__ == "__main__":
    main()
