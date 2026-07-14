from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from core.exceptions.base import AppException


def register_exception_handlers(app: FastAPI) -> None:
    """
    Register all application exception handlers.
    """

    @app.exception_handler(AppException)
    async def app_exception_handler(
        request: Request,
        exc: AppException,
    ):
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