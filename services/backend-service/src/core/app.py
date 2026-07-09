from fastapi import FastAPI

from api.router import router
from config.settings import get_settings
from core.logging.logger import setup_logging
from core.middleware.request_logging import RequestLoggingMiddleware
from core.lifespan import lifespan

import logging


def create_app() -> FastAPI:

    setup_logging()

    logger = logging.getLogger(__name__)

    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        lifespan=lifespan,
    )

    app.add_middleware(RequestLoggingMiddleware)

    app.include_router(router)

    return app