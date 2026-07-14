from uuid import UUID

from core.logging.app_logger import AppLogger
from core.logging.events import EventType

from domain.intersection.models import Intersection
from domain.intersection.repositories import IntersectionRepository
from domain.intersection.schemas import IntersectionCreate

from core.exceptions.intersection import (
    IntersectionAlreadyExistsError,
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
        
        intersection = self.repository.create(data)
        
        logger.event(
            EventType.INTERSECTION_CREATED,
            message="Creating intersection",
            intersection_id=str(intersection.id),
            name=intersection.name,
            city=intersection.city,
        )

        return intersection
    
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
            raise IntersectionAlreadyExistsError()

        return intersection
    
    def get_all(
        self,
    ) -> list[Intersection]:
        """
        Retrieve all intersections.
        """

        return self.repository.get_all()