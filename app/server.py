"""Application server module"""

# import logging
import uvicorn

from fastapi import FastAPI

from app.core import settings
from app.api.handlers.v1 import api_router

log_config = uvicorn.config.LOGGING_CONFIG

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(api_router, prefix=settings.API_V1_STR)


def init_server() -> None:
    """
    Configure logging and log format.
    Spin up the server.
    """
    # Log format
    log_config["formatters"]["access"][
        "fmt"
    ] = "[%(asctime)s.%(msecs)d] | %(levelname)s | [%(name)s:%(filename)s:%(lineno)d] - %(message)s"
    log_config["formatters"]["default"][
        "fmt"
    ] = "[%(asctime)s.%(msecs)d] | %(levelname)s | [%(name)s:%(filename)s:%(lineno)d] - %(message)s"

    # Date format
    date_fmt = "%Y-%m-%d:%H:%M:%S"
    log_config["formatters"]["default"]["datefmt"] = date_fmt
    log_config["formatters"]["access"]["datefmt"] = date_fmt

    # Run the server
    uvicorn.run(
        "app.server:app", log_config=log_config, host="0.0.0.0", port=9000, reload=True
    )
