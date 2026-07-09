from datetime import UTC, datetime

from fastapi import APIRouter

from config.settings import get_settings
from core.logging.app_logger import AppLogger
from core.logging.events import EventType

router = APIRouter()

logger = AppLogger(__name__)
settings = get_settings()


@router.get("/health")
def health_check():
    logger.event(
        EventType.HEALTH_CHECK,
        message="Health endpoint accessed",
    )

    return {
        "status": "healthy",
        "service": settings.app_name,
        "version": settings.app_version,
        "timestamp": datetime.now(UTC).isoformat(),
    }