from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions.base import AppException
from core.logging.app_logger import AppLogger
from core.logging.events import EventType

logger = AppLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all application exception handlers.
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ):
        
        logger.event(
            EventType.APPLICATION_ERROR,
            message=exc.message,
            error_code=exc.error_code,
            status_code=exc.status_code,
            method=request.method,
            path=request.url.path,
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "success": False,
                "error": {
                    "code": exc.error_code,
                    "message": exc.message,
                },
            },
        )