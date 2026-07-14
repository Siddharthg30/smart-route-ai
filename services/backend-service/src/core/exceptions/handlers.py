from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
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
    
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        
        errors = []

        for error in exc.errors():
            errors.append(
                {
                    "field": ".".join(
                        str(part)
                        for part in error["loc"]
                        if part != "body"
                    ),
                    "message": error["msg"],
                }
            )

        logger.event(
            EventType.VALIDATION_ERROR,
            message="Request validation failed",
            method=request.method,
            path=request.url.path,
        )

        return JSONResponse(
            status_code=422,
            content={
                "success": False,
                "error": {
                    "code": "VALIDATION_ERROR",
                    "message": "Request validation failed.",
                    "details": errors,
                },
            },
        )