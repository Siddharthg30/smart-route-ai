from http import HTTPStatus

from .base import AppException


class IntersectionAlreadyExistsError(AppException):
    status_code = HTTPStatus.CONFLICT
    error_code = "INTERSECTION_ALREADY_EXISTS"
    message = "Intersection already exists."


class IntersectionNotFoundError(AppException):
    status_code = HTTPStatus.NOT_FOUND
    error_code = "INTERSECTION_NOT_FOUND"
    message = "Intersection not found."