import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from core.context import request_id
from core.logging.app_logger import AppLogger
from core.logging.events import EventType

logger = AppLogger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Logs every incoming request and outgoing response.
    """

    async def dispatch(self, request: Request, call_next):
        req_id = str(uuid.uuid4())
        request_id.set(req_id)

        start_time = time.perf_counter()

        logger.event(
            EventType.REQUEST_STARTED,
            method=request.method,
            path=request.url.path,
            client=request.client.host if request.client else "unknown",
        )

        try:
            response = await call_next(request)

        except Exception as exc:
            duration = round((time.perf_counter() - start_time) * 1000, 2)

            logger.event(
                EventType.REQUEST_FAILED,
                message=str(exc),
                duration_ms=duration,
            )

            raise

        duration = round((time.perf_counter() - start_time) * 1000, 2)

        logger.event(
            EventType.REQUEST_COMPLETED,
            status=response.status_code,
            duration_ms=duration,
        )

        response.headers["X-Request-ID"] = req_id

        return response