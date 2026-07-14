from http import HTTPStatus


class AppException(Exception):
    """
    Base exception for all application-specific errors.
    """

    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR
    error_code: str = "INTERNAL_SERVER_ERROR"
    message: str = "An unexpected error occurred."

    def __init__(self, message: str | None = None):
        if message:
            self.message = message

        super().__init__(self.message)