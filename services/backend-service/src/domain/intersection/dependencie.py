from fastapi import Depends
from sqlalchemy.orm import Session

from api.dependencies.database import get_db

from .repositories import IntersectionRepository
from .services import IntersectionService


def get_intersection_repository(
    db: Session = Depends(get_db),
) -> IntersectionRepository:
    """
    Provide an IntersectionRepository instance.
    """

    return IntersectionRepository(db)

def get_intersection_service(
    repository: IntersectionRepository = Depends(
        get_intersection_repository,
    ),
) -> IntersectionService:
    """
    Provide an IntersectionService instance.
    """

    return IntersectionService(repository)