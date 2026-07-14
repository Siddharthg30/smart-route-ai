from uuid import UUID

from core.logging.app_logger import AppLogger
from core.logging.events import EventType

from domain.intersection.models import Intersection
from domain.intersection.repositories import IntersectionRepository
from domain.intersection.schemas import IntersectionCreate

from sqlalchemy.exc import IntegrityError

from core.exceptions.intersection import (
    IntersectionAlreadyExistsError,
    IntersectionNotFoundError,
)

logger = AppLogger(__name__)

class IntersectionService:
    """
    Handles business logic for intersections.
    """

    def __init__(
        self,
        repository: IntersectionRepository,
    ):
        self.repository = repository

    def create(
        self,
        data: IntersectionCreate,
    ) -> Intersection:
        """
        Create a new intersection.
        """

        existing = self.repository.get_by_name(
            data.name
        )

        if existing:
            raise IntersectionAlreadyExistsError()
        
        try:
            intersection = self.repository.create(data)

            self.repository.db.commit()

            self.repository.db.refresh(intersection)

            logger.event(
                EventType.INTERSECTION_CREATED,
                message="Creating intersection",
                intersection_id=str(intersection.id),
                name=intersection.name,
                city=intersection.city,
            )

            return intersection
        
        except IntegrityError:
            self.repository.db.rollback()

            raise IntersectionAlreadyExistsError()

        except Exception:
            self.repository.db.rollback()
            raise
    
    def get_by_id(
        self,
        intersection_id: UUID,
    ) -> Intersection:
        """
        Retrieve an intersection by its ID.
        """

        intersection = self.repository.get_by_id(
            intersection_id
        )

        if not intersection:
            raise IntersectionNotFoundError()

        return intersection
    
    def get_all(
        self,
    ) -> list[Intersection]:
        """
        Retrieve all intersections.
        """

        return self.repository.get_all()