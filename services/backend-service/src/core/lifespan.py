from contextlib import asynccontextmanager

from fastapi import FastAPI

from core.logging.app_logger import AppLogger
from core.logging.events import EventType

logger = AppLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Handles application startup and shutdown.
    """

    logger.event(
        EventType.APP_STARTED,
        message="Backend service started successfully.",
    )

    yield

    logger.event(
        EventType.APP_STOPPED,
        message="Backend service stopped.",
    )