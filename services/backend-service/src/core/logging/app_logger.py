import logging
from typing import Any

from core.context import request_id
from core.logging.events import EventType


class AppLogger:
    """
    Wrapper around Python's logging module.
    """

    def __init__(self, name: str) -> None:
        self.logger = logging.getLogger(name)

    def event(
        self,
        event: EventType,
        message: str = "",
        **kwargs: Any,
    ) -> None:
        """
        Log a structured application event.
        """

        current_request_id = request_id.get()

        if current_request_id:
            kwargs["request_id"] = current_request_id

        log_message = str(event)

        if message:
            log_message += f" | {message}"

        if kwargs:
            details = ", ".join(
                f"{key}={value}"
                for key, value in kwargs.items()
            )
            log_message += f" | {details}"

        self.logger.info(log_message)